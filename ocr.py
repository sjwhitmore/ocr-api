

import urllib.request

from flask import Flask, jsonify, request
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    image_url = request.form['image']
    img_path = image_url.split('/')[-1]
    urllib.request.urlretrieve(
       image_url,
       img_path)
    config = ('-l eng --oem 1 --psm 3')
    raw_result = pytesseract.image_to_string(Image.open(img_path), config=config)
    result = raw_result.replace('|', 'I')
    return {
        'statusCode': 200,
        'body': result
    }

if __name__ == '__main__':
    app.run(debug=True)

