from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id_Ciudad = db.Column(db.String(20), primary_key=True)
    Departamento_idDepartamento = db.Column(db.String(20), db.ForeignKey('departamento.idDepartamento'))


    def __init__(self,id_Ciudad):
        self.id_Ciudad = id_Ciudad


    def json(self):
        return {'id_Ciudad':self.id_Ciudad}
    
    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class Departamento(db.Model):
    __tablename__ = 'departamento'
    idDepartamento = db.Column(db.String(20), primary_key=True)
    ciudad = db.relationship('Ciudad', cascade='all, delete, delete-orphan')

    def __init__(self, idDepartamento):
        self.idDepartamento = idDepartamento

    def json(self):
        return {'idDepartamento': self.idDepartamento, 'ciudad': self.ciudad}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class CiudadSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ciudad
        include_relationships = True
        load_instance = True


class DepartamentoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Departamento
        include_relationships = True
        load_instance = True
