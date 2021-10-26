from flask_restful import Resource, reqparse
from flask import send_file
from PIL import Image

import json
import uuid
import os
import werkzeug
import pytesseract

class ImageResource(Resource):
    
    def get(self):
        return "Hello world", 200

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        
        args = parse.parse_args()
        
        image_file = args['file']
        f_name = str(uuid.uuid4()) + ".jpg"

        image_file.save(f_name)
        text_from_image = pytesseract.image_to_string( Image.open(f_name), lang='por')
        text = text_from_image.encode('utf-8').decode().replace('\n', ' ').replace('\t', ' ')
        return json.dumps({
            'text':  text,
            'filename': f_name 
        }, ensure_ascii=False).encode('utf8').decode(), 200