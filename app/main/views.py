from flask import render_template, redirect, url_for
from flask_login import login_required,current_user
from flask_wtf import form
from . import main
from ..models import Post, Upvote, User, Upvote, Downvote, Comment
from .forms import postForm, commentForm, vote

@main.route('/')
def index():
    posts=Post.query.all()
    product=Post.query.filter_by(category='product').all()
    idea=Post.query.filter_by(category='idea').all()
    business=Post.query.filter_by(category='business').all()
    
    return render_template('index.html', product=product, idea=idea, business=business, posts=posts)

@main.route('/posts')
def posts():
    posts=Post.query.all()
    likes=Upvote.query.all()
    user=current_user
    
    return render_template(posts=posts, likes=likes, user=user)

@main.route('/new_post', methods=['GET', 'POST'])
def new_post():
    form=postForm()
    if form.validate_on_submit():
        title=form.title.data
        post=form.post.data
        category=form.category.data
        user_id=current_user._get_current_object().id
        post_object=Post(title=title, post=post, category=category, user_id=user_id)
        post_object.save()

        return redirect(url_for('main.index'))

    return render_template('pitch.html', form=form)

@main.route('/comment/<init:id>', methods=['GET', 'POST'])
def comment(post_id):
    form=commentForm()
    post=Post.query.get(post_id)    
    user=User.query.all()
    comments=Comment.query.filter_by(post_id=post_id).all()
    if form.validate_on_submit():
        comment=form.comment.data
        post_id=post_id
        user_id=current_user._get_current_object().id
        new_comment=Comment(comment=comment, post=post, user_id=user_id)
        new_comment.save()
        new_comments=[new_comment]
        print(new_comments)
        return redirect(url_for('.comment'), post_id=post_id)

    return render_template('comment.html', form=form, post=post, user=user, comments=comments)

@main.route('/user')
def user():
    username=current_user.username
    user=User.query.filter_by(username=username).first()
    if user is None:
        return ('User not found')
    return render_template('profile.html', user=user)

@main.route('/like/<int:id>', methods=['POST', 'GET'])
def upvote(id):
    post=Post.query.get(id)
    new_upvote=Upvote(post=post, upvote=1)
    new_upvote.save()

    return redirect(url_for('main.posts'))
     
@main.route('/dislike/<int:id>', methods=['POST', 'GET'])
def downvote(id):
    post=Post.query.get(id)
    new_downvote=Downvote(post=post, downvote=1)
    new_downvote.save()

    return redirect(url_for(main.posts))

    

