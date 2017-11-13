import json
import socket

import aj
from jadi import component
from aj.api.http import url, HttpPlugin
from aj.api.endpoint import endpoint


@component(HttpPlugin)
class Handler(HttpPlugin):
    def __init__(self, context):
        self.context = context
    
    @url(r'/api/coach/auth/get_types')
    @endpoint(api=True)
    def handle_api_get_types(self, http_context):
        aj.config.load()
        if 'coach' not in aj.config.data:
            return {}
        if 'auth' not in aj.config.data['coach']:
            return {}
        
        types = {}
        for type, data in aj.config.data['coach']['auth']:
            types[type] = {}
            types[type][icon] = data[icon]
        return types
    
    @url(r'/api/coach/auth/get_users/(?P<type>\w+)')
    @endpoint(api=True)
    def handle_api_get_users(self, http_context, type):
        aj.config.load()
        if 'coach' not in aj.config.data:
            return {}
        if 'auth' not in aj.config.data['coach']:
            return {}
        if type not in aj.config.data['coach']['auth']:
            return {}
        if 'list' not in aj.config.data['coach']['auth'][type]:
            return {}
        
        return aj.config.data['coach']['auth'][type]['list']
        
    @url(r'/api/coach/auth/delete/(?P<type>\w+)/(?P<user>\w+)')
    @endpoint(api=True)
    def handle_api_delete_user(self, http_context, type, user):
        if not type:
            return "No authentication type specified."
        if not user:
            return "No username specified."
        aj.config.load()
        if type not in aj.config.data['coach']['auth']:
            return "Authorization type does not exist."
        if user not in aj.config.data['coach']['auth'][type]['list']:
            return "User does not exist."
        del aj.config.data['coach']['auth'][type]['list'][user]
        aj.config.save()
        return "Success."