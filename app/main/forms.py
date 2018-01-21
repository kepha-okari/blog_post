from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,ValidationError,TextAreaField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    '''
    class to create wtf form for receive and submit blog data
    '''
    title = StringField('Blog Title',validators=[Required()])
    blog = StringField('Blog',validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a feedback on a post
    '''
    opinion =  TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
