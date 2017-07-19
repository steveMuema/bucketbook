from store import Stores

class Register(object):
    def __init__(self, _firstName, _lastName, _email, _password, _index):
        self._firstName = _firstName
        self._lastName = _lastName
        self._email = _email
        self._password = _password
        self._index=_index

    def register_credentials(self):
        """returns data to be in the stores for credentials """
        return{
            'firstName': self._firstName,
            'lastName': self._lastName,
            'email': self._email,
            'password': self._password,
            '_index': self._index
            }


    def save_credentials(self):
        Stores.account_store.append(self.register_credentials())

    
        