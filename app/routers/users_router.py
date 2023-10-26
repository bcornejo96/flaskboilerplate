from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas.user_schema import UserRequestSchema
from app.controllers.users_controller import UserController


user_ns = api.namespace(
    name='Users',
    description= 'Rutas del modulo Users',
    path='/users'
)

schema_request = UserRequestSchema(user_ns)

@user_ns.route('')
@user_ns.doc(security='Bearer')
class Users(Resource):
    @jwt_required()
    @user_ns.expect(schema_request.all())
    def get(self):
        ''' Lista todos los usuarios '''
        query_params = schema_request.all().parse_args()
        controller = UserController()
        return controller.fetch_all(query_params)

    @jwt_required()
    @user_ns.expect(schema_request.create(), validate=True)    
    def post(self):
        ''' Creacion de un usuario '''
        controller = UserController()
        return controller.save(request.json)


@user_ns.route('/<int:id>')  
@user_ns.doc(security='Bearer')  
class UserById(Resource):
    @jwt_required()
    def get(self, id): 
        ''' Obtener un usuario por su id '''
        controller = UserController()
        return controller.find_by_id(id)

    @jwt_required()        
    @user_ns.expect(schema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un usuario '''
        controller = UserController()
        return controller.update(id, request.json)
    
    @jwt_required()
    def delete(self,id):
        ''' Inhabilitar un usuario por su id'''
        controller = UserController()
        return controller.remove(id)
    

@user_ns.route('/profile/me')
@user_ns.doc(security='Bearer')
class UserProfile(Resource):
    @jwt_required()
    def get(self):
        '''Obtener los datos del usuario conectado'''
        identity = get_jwt_identity()
        controller = UserController()
        return controller.profile_me(identity)
