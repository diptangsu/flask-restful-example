import requests
from pprint import pprint


BASE_URL = 'http://127.0.0.1:5000'

URL_ALL_STUDENTS = BASE_URL + '/students/'
URL_STUDENT_1 = BASE_URL + '/students/1/'
URL_STUDENT_111111 = BASE_URL + '/students/111111/'
URL_AUTH = BASE_URL + '/auth'


def print_response(response):
    try:
        print(response.request.method, response.url, response.status_code)
        pprint(response.json())
    except:
        pass
    finally:
        print('\n')


# authenticate user
response = requests.post(URL_AUTH, json={
    'username': 'Dip',
    'password': 'dip'
}, headers={
    'Content-Type': 'application/json'
})
# print_response(response)
auth_token = response.json().get('access_token')

# set headers for subsequent requests
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'JWT {auth_token}'
}

# check all students
response = requests.get(URL_ALL_STUDENTS, headers=headers)
print_response(response)


# check student 1
response = requests.get(URL_STUDENT_1, headers=headers)
print_response(response)


# check student 111111
response = requests.get(URL_STUDENT_1, headers=headers)
print_response(response)


# check POST student
response = requests.post(URL_ALL_STUDENTS, json={
    'username': 'Dip',
    'age': 23
}, headers=headers)
print_response(response)

# check POST student fail
response = requests.post(URL_ALL_STUDENTS, json={
    'username': 'Dip',
    'age': 23
}, headers=headers)
print_response(response)

# check PUT student
response = requests.put(URL_STUDENT_1, json={
    'username': 'Diptangsu',
    'age': 23
}, headers=headers)
print_response(response)

# check PUT student fail
response = requests.put(URL_STUDENT_111111, json={
    'username': 'Dip',
    'age': 23
}, headers=headers)
print_response(response)

# check DELETE student
response = requests.delete(URL_STUDENT_1, headers=headers)
print_response(response)

# check DELETE student fail
response = requests.delete(URL_STUDENT_111111, headers=headers)
print_response(response)
