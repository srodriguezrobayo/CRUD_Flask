from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class TipoUsuario(db.Model):
    __tablename__ = 'tipo_usuario'
    idTipo_usuario = db.Column(db.Integer, primary_key=True)
    Nombre_t_usuario = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    empresas = db.relationship('Empresa', cascade='all, delete, delete-orphan')

    def __init__(self, idTipo_usuario, Nombre_t_usuario, estado):
        self.idTipo_usuario = idTipo_usuario
        self.Nombre_t_usuario = Nombre_t_usuario
        self.estado = estado

    def json(self):
        return {'idTipo_usuario':self.idTipo_usuario, 'Nombre_t_usuario':self.Nombre_t_usuario, 'estado':self.estado, 'empresas':self.empresas}
    
    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)
    


class Empresa(db.Model):
    __tablename__ = 'empresa'
    Nit_empresa = db.Column(db.Integer, primary_key=True)
    Nombre_empresa = db.Column(db.String(20), nullable=False)
    Correoelectronico_empresa = db.Column(db.String(20), nullable=False)
    Password_empresa = db.Column(db.String(100), nullable=False)
    Telefono_empresa = db.Column(db.Integer, nullable=True)
    Ciudad_id_Ciudad = db.Column(db.Integer, db.ForeignKey('tipo_usuario.idTipo_usuario'))

    def __init__(self, Nit_empresa, Nombre_empresa, Password_empresa, Telefono_empresa, Ciudad_id_Ciudad):
        self.Nit_empresa = Nit_empresa
        self.Nombre_empresa = Nombre_empresa
        self.Correoelectronico_empresa = Correoelectronico_empresa
        self.Password_empresa = Password_empresa
        self.Telefono_empresa = Telefono_empresa
        self.Ciudad_id_Ciudad = Ciudad_id_Ciudad

    def json(self):
        return {'Nit_empresa':self.Nit_empresa, 'Nombre_empresa':self.Nombre_empresa, 'Correoelectronico_empresa':self.Correoelectronico_empresa, 'Password_empresa':self.Password_empresa, 'Telefono_empresa':self.Telefono_empresa, 'Ciudad_id_Ciudad':self.Ciudad_id_Ciudad}
    
    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)


class TipoUsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TipoUsuario
        include_relationships = True
        load_instance = True


class EmpresaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empresa
        include_relationships = True
        load_instance = True
