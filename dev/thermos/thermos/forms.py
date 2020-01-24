from flask_wtf import Form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired, url

class BookmarkForm(Form):
    # URLField represents a HTML5 URL input, to validate if the user has input a valid url
    url = URLField('url', validators=[DataRequired(), url()])
    # StringField represents an <input type="text"> html field
    description = StringField('description')