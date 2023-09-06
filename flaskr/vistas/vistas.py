from flask_restful import Resource
from ..modelos import db, Departamento, Ciudad, DepartamentoSchema, CiudadSchema
from flask import request

departamento_schema = DepartamentoSchema()
ciudad_schema = CiudadSchema()

class VistaDepartamentos(Resource):
    def get(self):
        return [departamento_schema.dump(Departamento) for Departamento in Departamento.query.all()]
    
    def post(self):
        nuevo_departamento = Departamento(idDepartamento=request.json['idDepartamento'],)
        db.session.add(nuevo_departamento)
        db.session.commit()
        return departamento_schema.dump(nuevo_departamento)


class VistaDepartamento(Resource):
    def get(self, idDepartamento):
        return departamento_schema.dump(Departamento.query.get_or_404(idDepartamento))
    
    def put(self, idDepartamento):
        departamento = Departamento.query.get_or_404(idDepartamento)
        departamento.idDepartamento = request.json.get('idTipo_usuario', departamento.idDepartamento)
        db.session.commit()
        return departamento_schema.dump(departamento)
    
    def delete(self, idDepartamento):
        departamento = Departamento.query.get_or_404(idDepartamento)
        db.session.delete(departamento)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaCiudades(Resource):
    def get(self):
        return [ciudad_schema.dump(Ciudad) for Ciudad in Ciudad.query.all()]
    
    def post(self):
        nuevo_ciudad = Ciudad(id_Ciudad=request.json['id_Ciudad'])
        db.session.add(nuevo_ciudad)
        db.session.commit()
        return ciudad_schema.dump(nuevo_ciudad)


class VistaCiudad(Resource):
    def get(self, id_Ciudad):
        return ciudad_schema.dump(Ciudad.query.get_or_404(id_Ciudad))
    
    def put(self, id_Ciudad):
        ciudad = Ciudad.query.get_or_404(id_Ciudad)
        ciudad.id_Ciudad = request.json.get('id_Ciudad', Ciudad.id_Ciudad)
        db.session.commit()
        return ciudad_schema.dump(ciudad)
    
    def delete(self, id_Ciudad):
        ciudad = Ciudad.query.get_or_404(id_Ciudad)
        db.session.delete(ciudad)
        db.session.commit()
        return 'Operacion exitosa', 204