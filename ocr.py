import json
import logging
import os
import urllib.request

import cv2
from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
import pytesseract

app = Flask(__name__)
CORS(app)

@app.route('/ocr', methods=['POST'])
def ocr():
    print("hi")
    req_data = json.loads(request.data)
    image_url = req_data.get("image")
    print('image url')
    print(image_url)
    img_path = image_url.split('/')[-1]
    urllib.request.urlretrieve(
       image_url,
       img_path)
    # load the example image and convert it to grayscale
    # image = cv2.imread(img_path)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #
    # # apply thresholding to preprocess the image
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #
    # # apply median blurring to remove any blurring
    # gray = cv2.medianBlur(gray, 3)
    #
    # # save the processed image in the /static/uploads directory
    # proc_path = 'proc_' + img_path
    # cv2.imwrite(proc_path, gray)

    # perform OCR on the processed image
    config = ('-l eng --oem 1 --psm 3')
    raw_result = pytesseract.image_to_string(Image.open(img_path), config=config)
    # it always gets "I" wrong
    result = raw_result.replace('|', 'I')
    print('result')
    print(result)
    # remove the processed image
    #os.remove(proc_path)
    # remove original image
    os.remove(img_path)
    return jsonify({
        'statusCode': 200,
        'text': result
    })

if __name__ == '__main__':
    logging.getLogger('flask_cors').level = logging.DEBUG
    app.run(host='0.0.0.0', port=8080, debug=True)
