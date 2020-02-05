from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from auth.security import authinticate, identity
from resources.student import Student


app = Flask(__name__)
app.secret_key = '$%^uke45f78v4ei#$%^&ydfg12734vgn35y65o2!@#$&^'
api = Api(app)
jwt = JWT(app, authinticate, identity)


api.add_resource(Student, '/students/', '/students/<int:student_id>/')


if __name__ == '__main__':
    app.run(debug=True)
