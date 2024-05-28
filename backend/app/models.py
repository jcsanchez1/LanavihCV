from ..app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Usuario(db.Model):
    """
    Modelo para la tabla 'usuarios'.
    """
    __tablename__ = 'usuarios'
    IdUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(50), nullable=False)
    ContraseñaHash = db.Column(db.String(255), nullable=False)
    NombreCompleto = db.Column(db.String(50), nullable=False)
    Iniciales = db.Column(db.String(4), nullable=False)
    Email = db.Column(db.String(100), nullable=True)
    Estado = db.Column(db.Integer, nullable=True)
    FechaCreacion = db.Column(db.DateTime, default=datetime.utcnow)
    FirmaPath = db.Column(db.String(255), nullable=True)
    FirmaSelloPath = db.Column(db.String(255), nullable=True)
    IdProfesion = db.Column(db.Integer, db.ForeignKey('profesiones.IdProfesion'), nullable=True)
    IdRol = db.Column(db.Integer, db.ForeignKey('roles.IdRol'), nullable=True)

    def set_password(self, password):
        """
        Genera un hash para la contraseña y lo guarda.
        """        
        self.ContraseñaHash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verifica si la contraseña ingresada coincide con el hash almacenado.
        """        
        return check_password_hash(self.ContraseñaHash, password)

class Rol(db.Model):
    """
    Modelo para la tabla 'roles'.
    """
    __tablename__ = 'roles'
    IdRol = db.Column(db.Integer, primary_key=True)
    NombreRol = db.Column(db.String(50), nullable=False)
    Descripcion = db.Column(db.Text, nullable=True)
    usuarios = db.relationship('Usuario', backref='rol', lazy=True)
    modulos = db.relationship('Modulo', secondary='rolesmodulos', backref=db.backref('roles', lazy='dynamic'))

class Modulo(db.Model):
    """
    Modelo para la tabla 'modulos'.
    """
    __tablename__ = 'modulos'
    IdModulo = db.Column(db.Integer, primary_key=True)
    NombreModulo = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.Text, nullable=True)

class RolModulo(db.Model):
    """
    Modelo para la tabla 'rolesmodulos'.
    """
    __tablename__ = 'rolesmodulos'
    IdRol = db.Column(db.Integer, db.ForeignKey('roles.IdRol'), primary_key=True)
    IdModulo = db.Column(db.Integer, db.ForeignKey('modulos.IdModulo'), primary_key=True)

class Auditoria(db.Model):
    """
    Modelo para la tabla 'auditoria'.
    """
    __tablename__ = 'auditoria'
    IdAuditoria = db.Column(db.Integer, primary_key=True)
    UsuarioId = db.Column(db.Integer, db.ForeignKey('usuarios.IdUsuario'), nullable=True)
    Accion = db.Column(db.String(50), nullable=False)
    Descripcion = db.Column(db.Text, nullable=True)
    FechaAccion = db.Column(db.DateTime, default=datetime.utcnow)
