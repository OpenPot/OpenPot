from flask import Blueprint, flash, redirect, request, render_template, url_for
from flask_login import login_required, login_user, logout_user
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length

from openpot.models.chef import Chef

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    error = None

    if form.validate_on_submit():

        if Chef.find_by_identity(request.form.get('username')):
            error = "Username is already in use."
        elif Chef.find_by_identity(request.form.get('email')):
            error = "Email is already in use."

        if error is None:
            chef = Chef()
            form.populate_obj(chef)
            chef.password = Chef.encrypt_password(request.form.get('password'))
            chef.save()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        chef = Chef.find_by_identity(request.form.get('identity'))

        if chef and chef.authenticated(password=request.form.get('password')):
            login_user(chef)
            flash("You have been logged in.")
            return redirect(url_for('index'))
        else:
            flash("Identity or password is incorrect.")

    return render_template('auth/login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('index'))


class RegisterForm(Form):
    username = StringField("Username",
                           (DataRequired(), Length(3, 24)))
    password = PasswordField("Password",
                             (DataRequired(), Length(8, 128)))
    email = StringField("Email",
                        (DataRequired(), Length(3, 255)))


class LoginForm(Form):
    identity = StringField("Email or Username",
                           (DataRequired(), Length(3, 255)))
    password = PasswordField("Password",
                             (DataRequired(), Length(8, 128)))
