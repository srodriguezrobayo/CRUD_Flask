from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Empleados(db.Model):
    id_empleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_empleado = db.Column(db.Integer, nullable=False)
    correo_elec_admin = db.Column(db.Date, nullable=False)
    password_empleado = db.Column(db.Time, nullable=False)
    tipo_usuario_idtipo_usuario = db.Column(db.Integer, db.ForeignKey('tipo_usuario.idTipo_usuario'))
    telefono_empleado = db.Column(db.Integer, nullable=False)
    genero_idgenero = db.Column(db.Integer, db.ForeignKey('genero.idGenero'))
    reservaciones = db.relationship('Reservacion', cascade='all, delete, delete-orphan')
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

class Lugar_reservacion(db.Model):
    id_direccion_lugarreserv = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_lugreserv = db.Column(db.String(128), nullable=False)
    ciudad_id_ciudad = db.Column(db.String(20), db.ForeignKey('ciudad.id_Ciudad'))
    reservaciones = db.relationship('Reservacion', cascade='all, delete, delete-orphan')

    def __init__(self, nom_lugaresreserv, ciudad_id_ciudad):
        self.nom_lugreserv = nom_lugaresreserv
        self.ciudad_id_ciudad = ciudad_id_ciudad

    def json(self):
        return {'id_direccion_lugreserv': self.id_direccion_lugreserv, 'nom_lugreserv': self.nom_lugreserv, 'ciudad_id_ciudad' : self.ciudad_id_ciudad}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)
class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_Cliente = db.Column(db.Integer, primary_key=True)
    Nombre_cliente = db.Column(db.String(20), nullable=False)
    Correoelectronico_cliente = db.Column(db.String(20), nullable=False)
    Password_cliente = db.Column(db.String(80), nullable=False)
    Telefono_cliente = db.Column(db.Integer, nullable=True)
    Genero_idGenero = db.Column(db.Integer, db.ForeignKey('genero.idGenero'))
    Ciudad_id_Ciudad = db.Column(db.String(20), db.ForeignKey('ciudad.id_Ciudad'))
    reservaciones = db.relationship('Reservacion', cascade='all, delete, delete-orphan')

    def __init__(self, id_Cliente, Nombre_cliente, Correoelectronico_cliente, Password_cliente, Telefono_cliente, Genero_idGenero, Ciudad_id_Ciudad ):
        self.id_Cliente = id_Cliente
        self.Nombre_cliente = Nombre_cliente
        self.Correoelectronico_cliente = Correoelectronico_cliente
        self.Password_cliente = Password_cliente
        self.Telefono_cliente = Telefono_cliente
        self.Genero_idGenero = Genero_idGenero
        self.Ciudad_id_Ciudad = Ciudad_id_Ciudad

    def json(self):
        return {'id_Cliente': self.id_Cliente, 'Nombre_cliente': self.Nombre_cliente, 'Correoelectronico_cliente': self.Correoelectronico_cliente, 'Password_cliente': self.Password_cliente, 'Telefono_cliente': self.Telefono_cliente , 'Genero_idGenero': self.Genero_idGenero, 'Ciudad_id_Ciudad': self.Ciudad_id_Ciudad }

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class Genero(db.Model):
    __tablename__ = 'genero'
    idGenero = db.Column(db.Integer, primary_key=True)
    Desc_genero = db.Column(db.String(20), nullable=False)
    clientes = db.relationship('Cliente', cascade='all, delete, delete-orphan')
    empleados= db.relationship('Empleados', cascade='all, delete, delete-orphan')

    def __init__(self, idGenero, Desc_genero):
        self.idGenero = idGenero
        self.Desc_genero = Desc_genero

    def json(self):
        return {'idGenero': self.idGenero, 'Desc_genero': self.Desc_genero, 'clientes': self.clientes}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id_Ciudad = db.Column(db.String(20), primary_key=True)
    Departamento_idDepartamento = db.Column(db.String(20), db.ForeignKey('departamento.idDepartamento'))
    empresas = db.relationship('Empresa', cascade='all, delete, delete-orphan')
    clientes = db.relationship('Cliente', cascade='all, delete, delete-orphan')
    lugares_reservacion = db.relationship('Lugar_reservacion', cascade='all, delete, delete-orphan')

    def __init__(self, id_Ciudad):
        self.id_Ciudad = id_Ciudad

    def json(self):
        return {'id_Ciudad': self.id_Ciudad}

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


class TipoUsuario(db.Model):
    __tablename__ = 'tipo_usuario'
    idTipo_usuario = db.Column(db.Integer, primary_key=True)
    Nombre_t_usuario = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    empleados = db.relationship('Empleados', cascade='all, delete, delete-orphan')

    def __init__(self, idTipo_usuario, Nombre_t_usuario, estado):
        self.idTipo_usuario = idTipo_usuario
        self.Nombre_t_usuario = Nombre_t_usuario
        self.estado = estado

    def json(self):
        return {'idTipo_usuario': self.idTipo_usuario, 'Nombre_t_usuario': self.Nombre_t_usuario, 'estado': self.estado,
                'empresas': self.empresas}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)


class Empresa(db.Model):
    __tablename__ = 'empresa'
    Nit_empresa = db.Column(db.Integer, primary_key=True)
    Nombre_empresa = db.Column(db.String(20), nullable=False)
    Correoelectronico_empresa = db.Column(db.String(20), nullable=False)
    Password_empresa = db.Column(db.String(100), nullable=False)
    Telefono_empresa = db.Column(db.Integer, nullable=True)
    Ciudad_id_Ciudad = db.Column(db.String(20), db.ForeignKey('ciudad.id_Ciudad'))
    reservaciones = db.relationship('Reservacion', cascade='all, delete, delete-orphan')

    def __init__(self, Nit_empresa, Nombre_empresa,Correoelectronico_empresa, Password_empresa, Telefono_empresa, Ciudad_id_Ciudad):
        self.Nit_empresa = Nit_empresa
        self.Nombre_empresa = Nombre_empresa
        self.Correoelectronico_empresa = Correoelectronico_empresa
        self.Password_empresa = Password_empresa
        self.Telefono_empresa = Telefono_empresa
        self.Ciudad_id_Ciudad = Ciudad_id_Ciudad

    def json(self):
        return {'Nit_empresa': self.Nit_empresa, 'Nombre_empresa': self.Nombre_empresa,
                'Correoelectronico_empresa': self.Correoelectronico_empresa, 'Password_empresa': self.Password_empresa,
                'Telefono_empresa': self.Telefono_empresa, 'Ciudad_id_Ciudad': self.Ciudad_id_Ciudad}

    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)


class Reservacion(db.Model):
    id_reservacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    servicio = db.Column(db.Integer, db.ForeignKey("servicio.id_servicio"))
    fecha_reservacion = db.Column(db.Date, nullable=False)
    hora_reservacion = db.Column(db.Time, nullable=False)
    lugar_reservacion = db.Column(db.Integer, db.ForeignKey('lugar_reservacion.id_direccion_lugarreserv'))
    empresa = db.Column(db.Integer, db.ForeignKey('empresa.Nit_empresa'))
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_Cliente'))
    valor = db.Column(db.Integer, nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id_empleado'))

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

class GeneroSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Genero
        include_relationships = True
        load_instance = True


class ClienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        include_relationships = True
        load_instance = True

class Lugar_reservacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Lugar_reservacion
        include_relationships = True
        load_instance = True


class EmpleadosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empleados
        include_relationships = True
        load_instance = True
