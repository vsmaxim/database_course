from common.resources import ModelResource, ListCreateResource, RetrieveUpdateResource
from api.authorization.models import Users, Groups
from flask import request, session


class UsersListView(ListCreateResource):
    data = Users


class LoginView(ModelResource):
    data = Users

    def post(self):
        credentials = request.json
        password = self.mapper.get_password_by_username(credentials["username"])
        if password == credentials["password"]:
            session['logged_in'] = True
            session['group'] = self.mapper.get_group_by_username(credentials["username"])
            session.permanent = True
            return session.get('group'), 200
        else:
            return None, 403