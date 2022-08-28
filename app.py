from flask import Flask,jsonify, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from Project.models.user import User
from Project.models.programs import Program
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from Project.models.tutor import Tutor
from Project.db import db


#application factory function
def create_app(config):
    app=Flask(__name__,static_url_path='/',static_folder='./static')
    app.config.from_object(config)





    from Project.users.index import users

    app.register_blueprint(users)


    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

  

   
    return app



# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# db.app = app
# db.init_app(app)
# db.create_all()
  



# Class that converts a SQLAlchemy model into a dictionary of corresponding auto_field
# Model Meta is basically used to change the behavior of your model fields like changing order options


# if __name__ == "__main__":
#     app.run(debug=True)
