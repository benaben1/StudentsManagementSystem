from flask_sqlalchemy import SQLAlchemy
from Project.db import db



class Program(db.Model):
    __tablename__ = "programs"
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String)
    time_of_schedule = db.Column(db.String)
    customer_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


    def __init__(self, program_name, time_of_schedule, customer_id):
        self.program_name = program_name
        self.time_of_schedule = time_of_schedule
        self.customer_id = customer_id
        

    def __repr__(self):
        return f"{self.id}"
