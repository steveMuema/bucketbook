from register import Register
class Account(object):
    """Account """
    def __init__(self, firstName, lastName, email, password):
        """ initializes the credentials of user"""
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

    def account_credentials(self, firstName, lastName, email, password):
        """ inherits attributes from register"""
        credentials = Register(
            _firstName = firstName,
            _lastName = lastName,
            _email = email,
            _password = password,
        )
        return credentials      
