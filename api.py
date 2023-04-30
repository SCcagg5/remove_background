from flask import Flask, request, send_file, Response
from rembg import remove
import io

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

    def generate_response():
        yield img_result_bytes.getvalue()

    response = Response(generate_response(), content_type='image/png')
    response.headers['Content-Disposition'] = 'attachment; filename=result.png'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
