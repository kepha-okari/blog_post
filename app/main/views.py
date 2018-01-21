from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User, Blog
from flask_login import login_required,current_user
from datetime import datetime, timezone
from .. import db
from .forms import BlogForm


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    # posts = Post.get_posts()
    return render_template('index.html', title = title )

@main.route('/new/blog', methods=['GET','POST'])
def new_blog():
    '''
    route to avail form for writing a new blog
    '''
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        new_blog = Blog(title = title, blog = blog )
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html',form = form)

#delete articles
@main.route('/delete/blog/<int:id>', methods=['GET','POST'])
def delete_blog(id):
    """
    view route to delete a selected post
    """
    article = Blog.query.filter_by(id=id).first()

    if article is None:
        abort(404)
        
    article.delete_blog()
    return redirect(url_for('main.index'))
