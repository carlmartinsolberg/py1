from flask import Flask
from flask_restful import Resource, Api

application = Flask(__name__)

@application.route("/")
def hello():
    return "OpenShift moramoramora!!"

if __name__ == "__main__":
    application.run()
