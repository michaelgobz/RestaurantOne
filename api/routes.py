from flask import Blueprint, request, make_response, jsonify, render_template, redirect, url_for, abort

from .auth.auth import Auth
from .sessions.sessions import Session
from .forms import SignupForm, LoginForm

AUTH = Auth()
SESSION = Session()

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/')
def home():
    return render_template('home.html')

# Authentication

@views.route('auth/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            AUTH.register_user(form.email, form.password,
                                  first_name=form.first_name, last_name=form.last_name)
        except ValueError:
            return make_response(jsonify({"message": f"{form.email} already registered"}), 400)
        
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@views.route('auth/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if not AUTH.valid_login(form.email, form.password):
            return jsonify({'error': 'Invalid email or password.'}), 401
        
        session_id = SESSION.create_session(form.email)
        if session_id is not None:
            response = jsonify({'email': form.email, 'message': "You were logged in successfully"})
            response.set_cookie('session_id', session_id)
            return render_template(url_for('home'))
        
    jsonify({'error': 'Unable to create session.'})
    return render_template('login.html', form=form)

@views.route('/auth/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Destroys a session
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = SESSION.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    SESSION.destroy_session(user.id)

    return redirect(url_for('login'))