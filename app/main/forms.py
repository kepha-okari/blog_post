from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,ValidationError
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog Title',validators=[Required()])
    blog = StringField('Blog',validators=[Required()])
    submit = SubmitField('Post')
