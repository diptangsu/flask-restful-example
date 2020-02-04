from flask import Flask, request, abort
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


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
    def get(self, student_id=None):
        if student_id is not None:
            return students.get(student_id) or abort(404)
        else:
            return students

    def post(self):
        data = request.get_json()


api.add_resource(Student, '/students/', '/students/<int:student_id>')


if __name__ == '__main__':
    app.run(debug=True)
