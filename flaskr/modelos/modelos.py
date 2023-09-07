from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Reservacion(db.Model):
    id_reservacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    servicio = db.Column(db.Integer, db.ForeignKey("servicio.id_servicio"))
    fecha_reservacion = db.Column(db.Date, nullable=False)
    hora_reservacion = db.Column(db.Time, nullable=False)
    lugar_reservacion = db.Column(db.String(128), nullable=False)
    empresa = db.Column(db.Integer, nullable=False)
    cliente = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Integer, nullable=False)
    empleado = db.Column(db.Integer, nullable=False)

    def __init__(self, servicio, fecha_reservacion, hora_reservacion, lugar_reservacion, empresa, cliente, valor, empleado):
        self.servicio = servicio
        self.fecha_reservacion = fecha_reservacion
        self.hora_reservacion = hora_reservacion
        self.lugar_reservacion = lugar_reservacion
        self.empresa = empresa
        self.cliente = cliente
        self.valor = valor
        self.empleado = empleado

    def json(self):
        return {'id_reservacion': self.id_reservacion, 'servicio': self.servicio, 'fecha_reservacion': self.fecha_reservacion, 'hora_reservacion': self.hora_reservacion, 'lugar_reservacion': self.lugar_reservacion, 'empresa': self.empresa, 'cliente': self.cliente, 'valor': self.valor, 'empleado': self.empleado}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class Servicio(db.Model):
    id_servicio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_servicio = db.Column(db.String(128), nullable=False)
    reservaciones = db.relationship('Reservacion', cascade='all, delete, delete-orphan')

    def __init__(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio

    def json(self):
        return {'id_servicio': self.id_servicio, 'nombre_servicio': self.nombre_servicio}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class ServicioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Servicio
        include_relationships = True
        load_instance = True

class ReservacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Reservacion
        include_relationships = True
        load_instance = True
