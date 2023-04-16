from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
from PIL import Image
import subprocess
import base64
import json
import io
import os

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
@app.route('/metadata', methods=['GET'])
def get_content_metadata():
    try:
        with open(os.path.join(CONTENT_DIR, 'metadata.json')) as f:
            return f.read()
    except FileNotFoundError:
        return '', 404

@app.route('/content/<path:path>', methods=["GET"])
def get_content(path):
    try:
        # Increment popularity count
        update_metadata(path)

        full_path = os.path.join(CONTENT_DIR, path)

        # If it's a directory, return a list of files and directories inside it
        if os.path.isdir(full_path):
            file_list = os.listdir(full_path)
            return {'files': file_list}

        # If it's a file, return the contents of the file
        with open(full_path) as f:
            return f.read()

    except FileNotFoundError:
        return '', 404

@app.route('/content', methods=['PATCH'])
def update_content():
    if request.json is None:
        return jsonify(success=False, error='Missing JSON request body')

    filename = request.json.get('filename', '')
    main_tag = request.json.get('main_tag', '')
    cover = request.json.get('cover', '')
    images = request.json.get('images', [])
    videos = request.json.get('videos', [])
    tags = request.json.get('tags', [])

    # Get the directory structure
    directory = os.path.join(CONTENT_DIR, main_tag, filename)

    # Update cover image
    if cover:
        try:
            cover_data = base64.b64decode(cover)
            cover_image = Image.open(io.BytesIO(cover_data))
            cover_image.save(os.path.join(directory, 'cover.avif'), format='AVIF')
        except Exception as e:
            return jsonify(success=False, error=str(e))

    # Update images
    for i, image in enumerate(images):
        try:
            image_data = base64.b64decode(image)
            image_file = io.BytesIO(image_data)
            image = Image.open(image_file)
            image.save(os.path.join(directory, 'images', f'image_{i}.avif'), format='AVIF')
        except Exception as e:
            return jsonify(success=False, error=str(e))

    # Update videos
    for i, video in enumerate(videos):
        try:
            video_data = base64.b64decode(video)
            video_file = os.path.join(directory, 'videos', f'video_{i}.heif')
            with open(video_file, 'wb') as f:
                subprocess.run(['ffmpeg', '-i', '-', '-f', 'heif', '-'], input=video_data, stdout=f, check=True)
        except Exception as e:
            return jsonify(success=False, error=str(e))

    # Update metadata
    metadata_path = os.path.join(CONTENT_DIR, METADATA_FILE)
    try:
        with open(metadata_path) as f:
            metadata = json.load(f)
    except FileNotFoundError:
        metadata = {}

    metadata[os.path.join(main_tag, filename)].update({
        'tags': tags,
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

    with open(metadata_path, 'w') as f:
        json.dump(metadata, f)

    return jsonify(success=True)


@app.route('/content', methods=['PUT'])
def create_content():
    if request.json is None:
        return jsonify(success=False, error='Missing JSON request body')

    filename = request.json.get('filename', '')
    main_tag = request.json.get('main_tag', '')
    cover = request.json.get('cover', '')
    images = request.json.get('images', [])
    videos = request.json.get('videos', [])
    tags = request.json.get('tags', [])

    # Create directory structure
    directory = os.path.join(CONTENT_DIR, main_tag, filename)
    os.makedirs(directory, exist_ok=True)
    os.makedirs(os.path.join(directory, 'images'), exist_ok=True)
    os.makedirs(os.path.join(directory, 'videos'), exist_ok=True)

    # Save cover image
    if cover:
        try:
            cover_data = base64.b64decode(cover)
            cover_image = Image.open(io.BytesIO(cover_data))
            cover_image.save(os.path.join(directory, 'cover.avif'), format='AVIF')
        except Exception as e:
            return jsonify(success=False, error=str(e))

    # Save images
    for i, image in enumerate(images):
        try:
            image_data = base64.b64decode(image)
            image_file = io.BytesIO(image_data)
            image = Image.open(image_file)
            image.save(os.path.join(directory, 'images', f'image_{i}.avif'), format='AVIF')
        except Exception as e:
            return jsonify(success=False, error=str(e))

    # Save videos
    for i, video in enumerate(videos):
        try:
            video_data = base64.b64decode(video)
            video_file = os.path.join(directory, 'videos', f'video_{i}.heif')
            with open(video_file, 'wb') as f:
                subprocess.run(['ffmpeg', '-i', '-', '-f', 'heif', '-'], input=video_data, stdout=f, check=True)
        except Exception as e:
            return jsonify(success=False, error=str(e))

    # Create file
    try:
        with open(os.path.join(directory, filename + '.md'), 'w') as f:
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
    'cover': os.path.join(main_tag, filename, 'cover', 'cover.avif'),
    'images': [os.path.join(main_tag, filename, 'images', f'image_{i}.avif') for i in range(len(images))],
    'videos': [os.path.join(main_tag, filename, 'videos', f'video_{i}.heif') for i in range(len(videos))],    'tags': tags,
    'popularity': 0,
    'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'sentiment': {
        'polarity': '',
        'subjectivity': '',
        'emotions': {
            'anger': '',
            'joy': '',
            'fear': '',
            'sadness': ''
        },
        'sentiment_categories': {
            'positive': '',
            'negative': '',
            'neutral': ''
        },
        'sentiment_keywords': '' # Keywords that contributed to the sentiment analysis
    },
    'targeting': {
        'age_range': {
            'min_age': '',
            'max_age': ''
        },
        'location': {
            'country': '',
            'city': '',
            'region': ''
        },
        'interests': '',
        'gender': '',
        'education_level': '',
        'income_level': '',
        'occupation': '',
        'marital_status': '',
        'parental_status': ''
    },
    'engagement': {
        'views': 0,
        'likes': 0,
        'comments': 0,
        'shares': 0
    }
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
