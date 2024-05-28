from functools import wraps
from flask import session, redirect, url_for, request, jsonify

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('api.login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(role_id):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_role' not in session or session['user_role'] != role_id:
                return jsonify({"message": "Unauthorized access"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
