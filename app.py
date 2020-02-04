from flask import Flask, request, abort
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required

from security import authinticate, identity


app = Flask(__name__)
app.secret_key = '$%^uke45f78v4ei#$%^&ydfg12734vgn35y65o2!@#$&^'
api = Api(app)
jwt = JWT(app, authinticate, identity)


students = {
    1: {
        'id': 1,
        'name': 'Diptangsu Goswami',
        'age': 23
    },
    2: {
        'id': 2,
        'name': 'Diptangsu Goswami',
        'age': 23
    },
    3: {
        'id': 3,
        'name': 'Diptangsu Goswami',
        'age': 23
    }
}


class Student(Resource):
    @jwt_required()
    def get(self, student_id=None):
        if student_id is not None:
            return students.get(student_id) or abort(404)
        else:
            return students

    @jwt_required()
    def post(self):
        data = request.get_json() or request.form
        student_id = len(students) + 1
        student = {
            'id': student_id,
            'name': data.get('name'),
            'age': data.get('age')
        }
        students[student_id] = student

        return student, 201


api.add_resource(Student, '/students/', '/students/<int:student_id>/')


if __name__ == '__main__':
    app.run(debug=True)
