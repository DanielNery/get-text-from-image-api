from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.image import ImageResource

app = Flask(__name__)
api = Api(app)

CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

api.add_resource(ImageResource, '/image')

if __name__ == '__main__':
    app.run()