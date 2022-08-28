from flask_sqlalchemy import SQLAlchemy


class CourseUnit(db.Model):
    __tablename__ = "courseUnit"
    id = db.Column(db.Integer, primary_key=True)
    course_unit_name = db.Column(db.String(25))
    programs_id = db.Column(
        db.Integer, db.ForeignKey('programs.id'), nullable=False)
    tutor_id = db.Column(db.Integer, db.ForeignKey(
        'tutor.id'), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, course_unit_name, programs_id):
        self.course_unit_name = course_unit_name
        self.programs_id = programs_id
       

    def __repr__(self):
        return f"{self.id}"
