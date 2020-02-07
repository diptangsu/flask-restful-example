from flask import request, abort
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


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


class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str
    )
    parser.add_argument(
        'age',
        type=int,
        required=True,
        help="This is a required field"
    )

    @jwt_required()
    def get(self, student_id=None):
        '''
        GET /students/ -> get all students
        GET /students/{id}/ -> get student with id=id
        '''
        if student_id is not None:
            return students.get(student_id) or abort(404)
        else:
            return students

    @jwt_required()
    def post(self):
        '''POST /students/ -> add a new student
        '''
        data = Student.parser.parse_args()
        student_id = len(students) + 1
        student_name = data.get('username')

        student_names_matched = (
            student['name'] == student_name
            for _, student in students.items()
        )
        if any(student_names_matched):
            return {
                'message': f'A student with username {student_name} already exists'
            }, 400

        student = {
            'id': student_id,
            'name': student_name,
            'age': data.get('age')
        }
        students[student_id] = student

        return student, 201

    @jwt_required()
    def put(self, student_id=None):
        '''PUT /students/{id} -> update student with id=id
        '''
        if student_id is not None:
            student = students.get(student_id)
            if student:
                data = Student.parser.parse_args()
                student.update(data)
                return student
        abort(404)

    @jwt_required()
    def delete(self, student_id=None):
        '''DELETE /students/{id} -> delete student with id=id
        '''
        global students
        if student_id is not None:
            if student_id in students:
                del students[student_id]
                return {'message': 'Student has been deleted'}
        abort(404)
