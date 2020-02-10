from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from auth.security import authinticate, identity
from resources.student import StudentResource


app = Flask(__name__)
app.secret_key = '$%^uke45f78v4ei#$%^&ydfg12734vgn35y65o2!@#$&^'
CORS(app)
api = Api(app)
jwt = JWT(app, authinticate, identity)


api.add_resource(StudentResource, '/students/', '/students/<int:student_id>/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
