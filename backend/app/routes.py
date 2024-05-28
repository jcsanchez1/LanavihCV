from flask import Blueprint, request, jsonify, session, redirect, url_for
from .models import db, Usuario, Rol, Modulo, RolModulo
from werkzeug.security import generate_password_hash, check_password_hash

# Define un Blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

@main_bp.route('/api/login', methods=['POST'])
def login():
    """
    Ruta para iniciar sesión. Verifica las credenciales del usuario.
    """
    data = request.json
    usuario = Usuario.query.filter_by(NombreUsuario=data['username']).first()
    if usuario and check_password_hash(usuario.ContraseñaHash, data['password']):
        session['user'] = usuario.IdUsuario  # Guarda el ID del usuario en la sesión
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@main_bp.route('/api/logout', methods=['POST'])
def logout():
    """
    Ruta para cerrar sesión. Elimina el usuario de la sesión.
    """
    session.pop('user', None)
    return jsonify({"message": "Logout successful"}), 200

@main_bp.route('/api/check-session', methods=['GET'])
def check_session():
    """
    Ruta para verificar si el usuario está autenticado.
    """
    if 'user' in session:
        return jsonify({"authenticated": True}), 200
    return jsonify({"authenticated": False}), 401