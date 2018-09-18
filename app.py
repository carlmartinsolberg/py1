#from flask import Flask
#from flask_restful import Resource, Api

#application = Flask(__name__)

#@application.route("/")
#def hello():
#    return "OpenShift moramoramora!!"

#if __name__ == "__main__":
#    application.run()


# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')