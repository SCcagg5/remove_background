from flask import Flask, request, send_file
from rembg import remove
import io
import base64

app = Flask(__name__)

@app.route('/detourer_image', methods=['POST'])
def detourer_image():
    if 'image' not in request.files:
        return {'error': 'Pas d\'image envoyée'}, 400

    image = request.files['image'].read()
    img = io.BytesIO(image)
    img_result = remove(img)
    img_result_bytes = io.BytesIO()
    img_result.save(img_result_bytes, format='PNG')
    img_result_bytes.seek(0)
    
    response = send_file(img_result_bytes, mimetype='image/png')
    response.headers['Content-Disposition'] = 'attachment; filename=result.png'
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
