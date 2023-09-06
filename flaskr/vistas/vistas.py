from flask_restful import Resource
from ..modelos import db, TipoUsuario, TipoUsuarioSchema, Empresa, EmpresaSchema
from flask import request

tipo_usuario_schema = TipoUsuarioSchema()
empresa_schema = EmpresaSchema()

class VistaTiposUsuarios(Resource):
    def get(self):
        return [tipo_usuario_schema.dump(TipoUsuario) for TipoUsuario in TipoUsuario.query.all()]
    
    def post(self):
        nuevo_tipo_usuario = TipoUsuario(idTipo_usuario=request.json['idTipo_usuario'], \
                                        Nombre_t_usuario=request.json['Nombre_t_usuario'], \
                                        estado=request.json['estado'])
        db.session.add(nuevo_tipo_usuario)
        db.session.commit()
        return tipo_usuario_schema.dump(nuevo_tipo_usuario)


class VistaTipoUsuario(Resource):
    def get(self, idTipo_usuario):
        return tipo_usuario_schema.dump(TipoUsuario.query.get_or_404(idTipo_usuario))
    
    def put(self, idTipo_usuario):
        tipo_usuario = TipoUsuario.query.get_or_404(idTipo_usuario)
        tipo_usuario.idTipo_usuario = request.json.get('idTipo_usuario', tipo_usuario.idTipo_usuario)
        tipo_usuario.Nombre_t_usuario = request.json.get('Nombre_t_usuario', tipo_usuario.Nombre_t_usuario)
        tipo_usuario.estado = request.json.get('estado', tipo_usuario.estado)
        db.session.commit()
        return tipo_usuario_schema.dump(tipo_usuario)
    
    def delete(self, idTipo_usuario):
        tipo_usuario = TipoUsuario.query.get_or_404(idTipo_usuario)
        db.session.delete(tipo_usuario)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaEmpresas(Resource):
    def get(self):
        return [empresa_schema.dump(Empresa) for Empresa in Empresa.query.all()]
    
    def post(self):
        nuevo_empresa = Empresa(Nit_empresa=request.json['Nit_empresa'], \
                                Nombre_empresa=request.json['Nombre_empresa'], \
                                Correoelectronico_empresa=request.json['Correoelectronico_empresa'], \
                                Password_empresa=request.json['Password_empresa'], \
                                Telefono_empresa=request.json['Telefono_empresa'], \
                                Ciudad_id_Ciudad=request.json['Ciudad_id_Ciudad'])
        db.session.add(nuevo_empresa)
        db.session.commit()
        return empresa_schema.dump(nuevo_empresa)


class VistaEmpresa(Resource):
    def get(self, Nit_empresa):
        return empresa_schema.dump(Empresa.query.get_or_404(Nit_empresa))
    
    def put(self, Nit_empresa):
        empresa = TipoUsuario.query.get_or_404(Nit_empresa)
        empresa.Nit_empresa = request.json.get('Nit_empresa', empresa.Nit_empresa)
        empresa.Nombre_empresa = request.json.get('Nombre_empresa', empresa.Nombre_empresa)
        empresa.Correoelectronico_empresa = request.json.get('Correoelectronico_empresa', empresa.Correoelectronico_empresa)
        empresa.Password_empresa = request.json.get('Password_empresa', empresa.Password_empresa)
        empresa.Telefono_empresa = request.json.get('Telefono_empresa', empresa.Telefono_empresa)
        empresa.Ciudad_id_Ciudad = request.json.get('Ciudad_id_Ciudad', empresa.Ciudad_id_Ciudad)
        db.session.commit()
        return empresa_schema.dump(empresa)
    
    def delete(self, Nit_empresa):
        empresa = Empresa.query.get_or_404(Nit_empresa)
        db.session.delete(empresa)
        db.session.commit()
        return 'Operacion exitosa', 204