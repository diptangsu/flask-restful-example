from models.user import User


users = [
    User('Dip', 'dip'),
    User('Dip2', 'dip'),
]

userid_mapping = {user.id: user for user in users}

usernamed_mapping = {user.username: user for user in users}


def authinticate(username, password):
    user = usernamed_mapping.get(username)
    if user and user.password == password:
        return user


def identity(payload):
    return userid_mapping[payload['identity']]
