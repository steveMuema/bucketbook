""" This module is used for importing app module and run it if the __name__ == '__main__' """

from app import app
import os
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()
