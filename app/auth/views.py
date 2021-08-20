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
            error='There is no user with that username'
            return render_template('login.html', error=error)
        password_correct=user.check_password(password)
        print(password_correct)
        if not password:
            error='You have entered a wrong password, please try again.'
            return render_template('login.html', error=error)
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
            error = 'All fields are required'
            return render_template('signup.html', error=error)
        if ' ' in username:
            error = 'Username should not contain spaces'
            return render_template('signup.html', error=error)
        if password != confirm_password:
            error = "Your passwords do not match"
            return render_template('signup.html', error=error)
        else:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                error = 'A user with that name already exists'
                return render_template('signup.html', error=error)
            user = User.query.filter_by(email=email).first()
            if user is not None:
                error = 'A user with that email already exists'
                return render_template('signup.html', error=error)
            user = User(username=username)
            user.set_password(password)
            user.save()

        return redirect(url_for('auth.login'))

    return render_template('signup.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


