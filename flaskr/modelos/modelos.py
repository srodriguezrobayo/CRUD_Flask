from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Empleados(db.Model):
    id_empleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_empleado = db.Column(db.Integer, db.ForeignKey("servicio.id_servicio"))
    correo_elec_admin = db.Column(db.Date, nullable=False)
    password_empleado = db.Column(db.Time, nullable=False)
    tipo_usuario_idtipo_usuario = db.Column(db.String(128), nullable=False)
    telefono_empleado = db.Column(db.Integer, nullable=False)
    genero_idgenero = db.Column(db.Integer, nullable=False)


    def __init__(self, nom_empleado, correo_elec_admin, password_empleado, tipo_usuario_idtipo_usuario, telefono_empleado, genero_idgenero ):
        self.nom_empleado = nom_empleado
        self.correo_elec_admin = correo_elec_admin
        self.password_empleado = password_empleado
        self.tipo_usuario_idtipo_usuario = tipo_usuario_idtipo_usuario
        self.telefono_empleado = telefono_empleado
        self.genero_idgenero = genero_idgenero


    def json(self):
        return {'id_empleado': self.id_empleado, 'nom_empleado': self.nom_empleado, 'password_empleado': self.password_empleado, 'tipo_usuario_idtipo_usuario': self.tipo_usuario_idtipo_usuario, 'telefono_empleado': self.telefono_empleado, 'genero_idgenero': self.genero_idgenero}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class lugar_reservacion(db.Model):
    id_direccion_lugreserv = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_lugreserv = db.Column(db.String(128), nullable=False)
    ciudad_id_ciudad = db.relationship('ciudad_id_ciudad', cascade='all, delete, delete-orphan')

    def __init__(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio

    def json(self):
        return {'id_direccion_lugreserv': self.id_direccion_lugreserv, 'nom_lugreserv': self.nom_lugreserv, 'ciudad_id_ciudad' : self.ciudad_id_ciudad}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class ServicioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = lugar_reservacion
        include_relationships = True
        load_instance = True

class ReservacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empleados
        include_relationships = True
        load_instance = True
