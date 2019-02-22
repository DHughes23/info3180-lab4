import os
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed, FileField

class UploadForm(FlaskForm):
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg', 'png'])])