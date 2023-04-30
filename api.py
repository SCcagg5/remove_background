from bottle import route, run, request, response, HTTPResponse
from rembg import remove
import io
import json

@route('/detourer_image', method='POST')
def detourer_image():
    if 'image' not in request.files:
        error_response = {'error': 'Pas d\'image envoyée'}
        return HTTPResponse(body=json.dumps(error_response), status=400, content_type='application/json')

    image = request.files.get('image')
    img = io.BytesIO(image.file.read())
    img_result = remove(img)
    img_result_bytes = io.BytesIO()
    img_result.save(img_result_bytes, format='PNG')
    img_result_bytes.seek(0)

    response.content_type = 'image/png'
    response.set_header('Content-Disposition', 'attachment; filename=result.png')

    return img_result_bytes.getvalue()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
