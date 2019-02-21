import os
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(FlaskForm):
    photo = FileField('image',validators=[FileRequired(),FileAllowed(['jpg', 'png'], "Only Pictures allowed")])