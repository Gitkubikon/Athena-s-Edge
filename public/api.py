from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'sabalimbalim'  # Set a secret key for JWT
jwt = JWTManager(app)  # Initialize JWT

CONTENT_DIR = 'content'
METADATA_FILE = 'metadata.json'
metadata = {}

# Generate JWT token
@app.route('/login', methods=['POST'])
def login():

    if request.json is not None:
        password = request.json.get('password', '')
        username = request.json.get('username', '')
    else:
        password = ''
        username = ''
    if username == 'user' and password == 'pass':
        token = create_access_token(identity=username)
        return jsonify(success=True, token=token)
    else:
        return jsonify(success=False, error='Invalid credentials'), 401

def update_metadata(path):
    # Load metadata
    metadata_path = os.path.join(CONTENT_DIR, METADATA_FILE)
    try:
        with open(metadata_path) as f:
            metadata = json.load(f)
    except FileNotFoundError:
        metadata = {}

    # Increment popularity count
    metadata[path]['popularity'] += 1

    # Save metadata
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f)

# Protected routes
@app.route('/content', methods=['GET'])
def get_content_list():
    try:
        content_list = os.listdir(CONTENT_DIR)
        return jsonify(content_list)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/content/<path:path>', methods=["GET"])
def get_content(path):
    try:
        # Increment popularity count
        update_metadata(path)

        with open(os.path.join(CONTENT_DIR, path)) as f:
            return f.read()
    except FileNotFoundError:
        return '', 404

@app.route('/content/<path:path>', methods=['POST'])
@jwt_required()
def save_content(path):
    if request.json is not None:
        content = request.json.get('content', '')
    else:
        content = ''
    try:
        with open(os.path.join(CONTENT_DIR, path), 'w') as f:
            f.write(content)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/content', methods=['PUT'])
def create_content():
    if request.json is None:
        return jsonify(success=False, error='Missing JSON request body')

    filename = request.json.get('filename', '')
    main_tag = request.json.get('main_tag', '')
    tags = request.json.get('tags', [])

    # Create directory structure
    directory = os.path.join(CONTENT_DIR, main_tag)
    os.makedirs(directory, exist_ok=True)

    # Create file
    try:
        with open(os.path.join(directory, filename), 'w') as f:
            f.write('')
    except Exception as e:
        return jsonify(success=False, error=str(e))

    # Add metadata
    metadata_path = os.path.join(CONTENT_DIR, METADATA_FILE)
    try:
        with open(metadata_path) as f:
            metadata = json.load(f)
    except FileNotFoundError:
        metadata = {}

    metadata[os.path.join(main_tag, filename)] = {
        'main_tag': main_tag,
        'tags': tags,
        'popularity': 0,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    with open(metadata_path, 'w') as f:
        json.dump(metadata, f)

    return jsonify(success=True)

@app.route('/content/<path:path>', methods=['DELETE'])
def delete_content(path):
    try:
        os.remove(os.path.join(CONTENT_DIR, path))

        # Delete metadata
        metadata_path = os.path.join(CONTENT_DIR, METADATA_FILE)
        with open(metadata_path) as f:
            metadata = json.load(f)
        del metadata[path]
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f)

        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    dev_mode = False
    if dev_mode:
        app.run(debug=True, port=3000)
    else:
        app.run(host='0.0.0.0', port=80)
