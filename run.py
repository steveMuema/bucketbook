""" This module is used for importing app module and run it if the __name__ == '__main__' """

from app import app
if __name__ == "__main__":
    app.run(debug=True)
