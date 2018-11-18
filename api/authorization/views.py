from common.resources import ModelResource, ListCreateResource, RetrieveUpdateResource
from flask_restful import Resource
from api.authorization.models import Users, Groups
from flask import request, session


class UsersListView(ListCreateResource):
    data = Users


class GroupsListView(ListCreateResource):
    data = Groups


class LoginView(ModelResource):
    data = Users

    def post(self):
        credentials = request.json
        password = self.mapper.get_password_by_username(credentials["username"])
        if password == credentials["password"]:
            session['logged_in'] = True
            session['group'] = self.mapper.get_group_by_username(credentials["username"])
            session.permanent = True
            return {"group": session.get('group')}, 200
        else:
            return None, 403


class LogoutView(Resource):

    def post(self):
        session['logged_in'] = False
        session['group'] = None
        return None, 200
