from bottle import route, run, request, response, HTTPResponse
from rembg import remove
import io
import json
import tempfile
import os

@route('/detourer_image', method='POST')
def detourer_image():
    if 'image' not in request.files:
        error_response = {'error': 'Pas d\'image envoyée'}
        return HTTPResponse(body=json.dumps(error_response), status=400, content_type='application/json')

    image = request.files.get('image')

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as img_temp:
        img_temp.write(image.file.read())
        img_temp.flush()
        img_temp_path = img_temp.name

    with open(img_temp_path, 'rb') as img_file:
        img_result_bytes = io.BytesIO(remove(img_file.read()))

    os.remove(img_temp_path)

    response.content_type = 'image/png'
    response.set_header('Content-Disposition', 'attachment; filename=result.png')

    return img_result_bytes.getvalue()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
