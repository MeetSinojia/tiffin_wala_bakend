# app/models/user.py
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # In a real application, you'd use a database
    users = {
        'test': 'test'
    }

    @classmethod
    def find_by_username(cls, username):
        if username in cls.users:
            return cls(username, cls.users[username])
        return None

    def check_password(self, password):
        return self.password == password
