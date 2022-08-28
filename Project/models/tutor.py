from flask_sqlalchemy import SQLAlchemy
from Project.db import db

class Tutor(db.Model):
    __tablename__ = "tutor"
    id = db.Column(db.Integer, primary_key=True)
    tutors_name = db.Column(db.String(25))
    notes = db.Column(db.String(225))
    results = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self,id,):
        self.tutors_name = tutors_name
        self.notes = notes
        self.results = results
        self.user_id= user_id
       

    def __repr__(self):
        return f"{self.id}"


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

 


db.create_all()
