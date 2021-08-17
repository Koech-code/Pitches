from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user
from app.auth import auth
from app.models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        form=request.form
        username=form.get('username')
        password=form.get('password')
        print(username)
        user=User.query.filter_by(username=username).first()
        if user is None:
            UserNotFoundError='There is no user with that username'
            return render_template('login.html', error=UserNotFoundError)
        password_correct=user.check_password(password)
        print(password_correct)
        if not password:
            passwordError='You have entered a wrong password, please try again.'
            return render_template('login.html', error=passwordError)
        login_user(user)
        return redirect('/')

    return render_template('/login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        email = form.get('email')
        password = form.get('password')
        confirm_password = form.get('confirm_password')
        if username is None or password is None or email is None or confirm_password is None:
            fieldsBlankError = 'All fields are required'
            return render_template('signup.html', error=fieldsBlankError)
        if ' ' in username:
            spaceError = 'Username should not contain spaces'
            return render_template('signup.html', error=spaceError)
        if password != confirm_password:
            matchError = "Your passwords do not match"
            return render_template('signup.html', error=matchError)
        else:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                usernameError = 'A user with that name already exists'
                return render_template('signup.html', error=usernameError)
            user = User.query.filter_by(email=email).first()
            if user is not None:
                mailError = 'A user with that email already exists'
                return render_template('signup.html', error=mailError)
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect(url_for('auth.login'))



