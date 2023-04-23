from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import json
import os

app = Flask(__name__)

CORS(app)
app.config['SECRET_KEY'] = 'sabalimbalim'  # Set a secret key for JWT
jwt = JWTManager(app)  # Initialize JWT
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600

CONTENT_FOLDER = "content"
METADATA_FILE = "metadata.json"

# Generate JWT token
@app.route('/login', methods=['POST'])
def login():
    with open('config.json', 'r') as f:
        config = json.load(f)
    if request.json is not None:
        password = request.json.get('password', '')
        username = request.json.get('username', '')
    else:
        password = ''
        username = ''
    if username in config['users'] and password == config['users'][username]:
        token = create_access_token(identity=username)
        return jsonify(success=True, token=token)
    else:
        return jsonify(success=False, error='Invalid credentials'), 401

# Protected routes
@app.route('/metadata', methods=['GET'])
def get_content_metadata():
    try:
        with open(os.path.join(CONTENT_FOLDER, 'metadata.json')) as f:
            return f.read()
    except FileNotFoundError:
        return 'Metadata not found', 404

@app.route('/articles/<category>/<article>', methods=['GET'])
def get_article(category, article):
    article_folder = os.path.join(CONTENT_FOLDER, category, article)
    if not os.path.exists(article_folder):
        return jsonify({"message": "Article not found"}), 404

    with open(os.path.join(article_folder, "index.md"), "r") as f:
        content = f.read()

    metadata = load_metadata()
    if article not in metadata[category]:
        return jsonify({"message": "Metadata not found for article"}), 404


    # if article not in metadata or "engagement" not in metadata[category][article]:
    #     return jsonify({"message": "Metadata not found for article or engagement key not found"}), 404
    # if "views" not in metadata[category][article]["engagement"]:
    #     metadata[category][article]["engagement"]["views"] = 0
    # metadata[category][article]["engagement"]["views"] += 1


    save_metadata(metadata)

    return jsonify({"content": content, "metadata": metadata[category][article]}), 200



@app.route('/articles/<category>/<article>', methods=['PATCH'])
@jwt_required()
def patch_article(category, article):
    article_folder = os.path.join(CONTENT_FOLDER, category, article)
    if not os.path.exists(article_folder):
        return jsonify({"message": "Article not found"}), 404

    if request.json is not None:
        content = request.json.get('content', '')
        print(content)
        with open(os.path.join(article_folder, "index.md"), "w") as f:
            f.write(content)

    metadata = load_metadata()
    if article not in metadata[category]:
        return jsonify({"message": "Metadata not found for article"}), 404

    # req_data = request.get_json()
    # metadata[category][article].update(req_data)
    metadata[category][article]["modified_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_metadata(metadata)

    return jsonify({"metadata": metadata[category][article]}), 200


@app.route('/articles/<category>/<article>', methods=['PUT'])
@jwt_required()
def put_article(category, article):
    article_folder = os.path.join(CONTENT_FOLDER, category, article)
    if os.path.isdir(article_folder):
        return jsonify({"message": "Article already exists"}), 409

    os.makedirs(article_folder, exist_ok=True)

    with open(os.path.join(article_folder, "index.md"), "w") as f:
        f.write("")

    content_type = request.content_type
    if content_type == 'application/json':
        payload = request.get_json()
    else:
        payload = None

    template = None
    with open(os.path.join(CONTENT_FOLDER, "mt.json"), "r") as f:
        template = json.load(f)

    metadata = load_metadata()
    if category not in metadata:
        metadata[category] = {}
    if article not in metadata[category]:
        metadata[category][article] = template.copy()

    if payload:
        metadata[category][article].update(payload)

    for key in template:
        if key not in metadata[category][article]:
            metadata[category][article][key] = template[key]

    metadata[category][article]["created_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_metadata(metadata)

    return jsonify({"metadata": metadata[category][article]}), 201


@app.route("/media/<category>/<article>/<media_type>/<filename>", methods=["PUT"])
@jwt_required()
def put_media(category, article, media_type, filename):
    if media_type not in ["images", "videos"]:
        return f"{media_type} not allowed", 400

    if media_type == "cover" or media_type == "background":
        media_dir = os.path.join(CONTENT_FOLDER, category, article)
    else:
        media_dir = os.path.join(CONTENT_FOLDER, category, article, media_type)

    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

    file_path = os.path.join(media_dir, filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "wb") as f:
        f.write(request.data)

    # Update metadata for the uploaded image
    metadata = load_metadata()
    metadata[category][article][media_type].append(file_path)
    metadata[category][article]["modified_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_metadata(metadata)

    return jsonify({"message": "Media uploaded successfully"}), 201



@app.route("/media/<category>/<article>/<media_type>/<filename>", methods=["GET"])
@jwt_required()
def get_media(category, article, media_type, filename):
    if media_type not in ["images", "videos"]:
        return f"{media_type} not allowed", 400

    if media_type == "cover":
        media_dir = os.path.join(CONTENT_FOLDER, category, article)
    else:
        media_dir = os.path.join(CONTENT_FOLDER, category, article, media_type)

    if not os.path.exists(media_dir):
        return f"Media not found for {category}/{article}/{media_type}/{filename}", 404

    file_path = os.path.join(media_dir, filename)

    if not os.path.exists(file_path):
        return f"Media not found for {category}/{article}/{media_type}/{filename}", 404

    return send_from_directory(media_dir, filename), 200


@app.route('/media/<category>/<article>/<media_type>/<media>', methods=['DELETE'])
@jwt_required()
def delete_media(category, article, media_type, media):
    # Check if article and media exist

    if media_type == "cover":
        media_path = os.path.join(CONTENT_FOLDER, category, article, f"{media}")
    else:
        media_path = os.path.join(CONTENT_FOLDER, category, article, media_type, f"{media}")

    if not os.path.exists(media_path):
        return f"{media_type} with id {media} not found for article {article} in category {category}", 404

    # Delete the media file
    os.remove(media_path)

    # Update metadata for the deleted media
    metadata = load_metadata()
    if media_type not in metadata[category][article]:
        metadata[category][article][media_type] = {}
    metadata[category][article][media_type].remove(media_path)
    metadata[category][article]["modified_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_metadata(metadata)

    return f"{media_type} with id {media} deleted for article {article} in category {category}", 200


@app.route('/articles/<category>/<article>', methods=['DELETE'])
@jwt_required()
def delete_article(category, article):
    article_folder = os.path.join(CONTENT_FOLDER, category, article)
    if not os.path.exists(article_folder):
        return jsonify({"message": "Article not found"}), 404

    metadata = load_metadata()
    if article not in metadata[category]:
        return jsonify({"message": "Metadata not found for article"}), 404

    os.system("rm -r {}".format(article_folder))
    del metadata[category][article]
    save_metadata(metadata)

    return jsonify({"message": "Article deleted"}), 200


def load_metadata():
    metadata = {}
    try:
        with open(os.path.join(CONTENT_FOLDER, METADATA_FILE), "r") as f:
            metadata = json.load(f)
    except FileNotFoundError:
        print(f"Metadata file {METADATA_FILE} not found")
    except json.JSONDecodeError as e:
        print(f"Error loading metadata file: {e}")
    return metadata


def save_metadata(metadata):
    with open(os.path.join(CONTENT_FOLDER, METADATA_FILE), "w") as f:
        json.dump(metadata, f)


if __name__ == '__main__':
    dev_mode = False
    if dev_mode:
        app.run(debug=True, port=3000)
    else:
        app.run(host='0.0.0.0', port=80)
