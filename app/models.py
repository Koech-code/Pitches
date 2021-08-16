from datetime import datetime
from flask_login import UserMixin, current_user, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager

class User():
    __tablename__='users'

class Post():
    __tablename__='posts'

class Comment():
    __tablename__='comments'

class Upvote():
    __tablename__='upvotes'

class Downvote():
    __tablename__='downvotes'
    