class User:

    _users = 0

    def __init__(self, username, password):
        User._users += 1
        self.id = User._users
        self.username = username
        self.password = password

    def __repr__(self):
        return f'{self.id}: {self.username}'
