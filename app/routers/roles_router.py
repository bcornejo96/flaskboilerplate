from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from http import HTTPStatus
from app.controllers.roles_controller import RoleController
from app.schemas.roles_schema import RoleRequestSchema


role_ns = api.namespace(
    name = 'Roles',
    description= 'Rutas del modulo Roles',
    path = '/roles'
)


schema_request = RoleRequestSchema(role_ns)


# CRUD

@role_ns.route('')
@role_ns.doc(security='Bearer')
class Roles(Resource):
    #dispatch
    
    def get(self):
        ''' Listar todos los roles '''
        controller = RoleController()
        return controller.fetch_all()

    
    @role_ns.expect(schema_request.create(), validate=True)
    def post(self):
        ''' Creacion de un rol '''
        controller = RoleController()
        return controller.save(request.json)
    
    
@role_ns.route('<int:id>')
@role_ns.doc(security='Bearer')
class RoleById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un rol por su ID '''
        controller = RoleController()
        return controller.find_by_id(id)

    # def put(self, id):
    #     ''' Actualizar un rol por su ID '''
    #     return f' Actualizar {str(id)}' 
    @jwt_required()
    @role_ns.expect(schema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un rol por su ID, enviando el objeto parcial '''
        controller = RoleController()
        return controller.update(id, request.json)
    
    
    @jwt_required()
    def delete(self, id):
        ''' Inhabilitar un rol por su ID '''
        controller = RoleController()
        return controller.remove(id)


#lISTAR(GET)

# @app.route('/roles', methods=['GET'])
# def list_roles():
#     return 'Listado de roles'


#CREACION(POST)
# @app.route('/roles', methods=['POST'])
# def create_roles():
#     return 'Creacion de rol', HTTPStatus.CREATED

#ACTUALIZACION
# @app.route('/role/<int:id>', methods=['PUT', 'PATCH'])
# def update_roles(id):
#     return f' Actualizar {str(id)}'   


#ELIMINAR
# @app.route('/role/<int:id>', methods=['DELETE'])
# def delete_roles(id):
#     return f' Eliminar {str(id)}', HTTPStatus.OK


#La publicacion con el id x que se encuentra en la categoria Y
# /post/<int:category_id>/<int:post_id> 
