import requests
from PIL import Image
import io
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/cover/process', methods=['POST'])
def process_cover_art():
    data = request.json
    image_url = data.get('image_url')
    target_size = data.get('size', 300)  
    
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image = Image.open(io.BytesIO(response.content))
        
        # Resize maintaining aspect ratio
        image.thumbnail((target_size, target_size), Image.Resampling.LANCZOS)
        
        # Save to bytes
        output = io.BytesIO()
        image.save(output, format='JPEG', quality=85)
        processed_image_data = output.getvalue()
        
        return {
            "status": "success",
            "image_data": processed_image_data.hex(),  # Send as hex for JSON
            "dimensions": image.size,
            "format": "JPEG"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)