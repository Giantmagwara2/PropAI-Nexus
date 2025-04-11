from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from your_model import db, User, Role

app = Flask(__name__)
app.config['SECURITY_TWO_FACTOR'] = True
# ...other config options...

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
