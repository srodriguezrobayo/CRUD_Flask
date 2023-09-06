from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum

db = SQLAlchemy()

class Servicio(db.Model):
    id_servicio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_servicio = db.Column(db.String(128), nullable=False)
    def __init__(self, nombre_servicio):
        self.nombre_servicio=nombre_servicio
    def json(self):
        return {'id_servicio':self.id_servicio, 'nombre_servicio':self.nombre_servicio}
    def __str__(self):
        return str(self.__class__)+':'+str(self.__dict__)

class ServicioSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Servicio
        include_relationships = True
        load_instance = True