from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app, version='1.0', title='API', description='A simple API on gunicorn')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'gunicorn'}

if __name__ == '__main__':
    app.run(debug=True)

