from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User, Blog, Comment
from flask_login import login_required,current_user
from datetime import datetime, timezone
from .. import db
from .forms import BlogForm,CommentForm


# Views index
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    posts = Blog.get_posts()
    return render_template('index.html', title = title, posts=posts )

# view function to render a selected article and its comments
@main.route('/post/<int:id>', methods=['GET','POST'])
def single_line(id):
    '''
    View function to return a single article
    '''
    article = Blog.query.get(id)
    title = "article"
    comments = Comment.get_comments(id)

    return render_template('single-blog.html',article = article,title = title, comments=comments)

# view route to post a blog
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

#commenting route
@main.route('/post/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):

    '''
    View new comment function that returns a page with a form to create a comment for the specified post
    '''
    post = Blog.query.filter_by(id=id).first()

    if post is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comment( opinion=opinion, articles_id=id, user_id=current_user.id)
        new_comment.save_comment()

        return redirect(url_for('main.index'))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)

#delete selected comment
@main.route('/delete/comment/<int:id>', methods=['GET','POST'])
def delete_selected_comment(id):
    """
    view route to delete a selected comment
    """
    comment = Comment.query.get(id)
    comment.delete_comment(id)

    return redirect(url_for('main.index'))
