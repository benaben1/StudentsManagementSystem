from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from flask import Flask,jsonify, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from Project.models.user import User
from Project.models.programs import Program
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from Project.models.tutor import Tutor
from Project.db import db


class CourseUnit(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = CourseUnit
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    course_unit_name = fields.String(required=True)


