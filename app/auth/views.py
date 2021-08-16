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
            return render_template('login.html', UserNotFoundError=UserNotFoundError)
        password_correct=user.check_password(password)
        print(password_correct)
        if not password:
            passwordError='You have entered a wrong password, please try again.'
            return render_template('login.html', passwordError=passwordError)
        login_user(user)
        return redirect('/')

    return render_template('/login.html')



