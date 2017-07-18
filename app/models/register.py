from store import Stores

class Register(object):
    def __init__(self, _firstName, _lastName, _email, _password):
        self._firstName = _firstName
        self._lastName = _lastName
        self._email = _email
        self._password = _password

    def register_credentials(self):
        """returns data to be in the stores for credentials """
        return{
            'firstName': self._firstName,
            'lastName': self._lastName,
            'email': self._email,
            'password': self._password
            }

    def save_credentials(self):
        Stores.credentials.append(self.register_credentials())