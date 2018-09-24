from pyramid.view import view_config
from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPFound

USERS = {
    'admin': 'password'
}

import logging
log = logging.getLogger(__name__)

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    log.debug(request)    
    log.debug('User authenticated: ')
    log.debug(request.authenticated_userid)    
    if request.authenticated_userid:
        return {'user': 'Emanuel Pais'}
    headers = forget(request)
    return HTTPFound(location='/login', headers=headers)    

@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    if request.method == 'POST':
        login = request.params.get('login')
        password = request.params.get('password')        
        if login and USERS.get(login) == password:
            headers = remember(request, login)
            return HTTPFound('/', headers=headers)
    return {}    

@view_config(route_name='logout', renderer='templates/logout.jinja2')
def logout(request):
    headers = forget(request)
    return HTTPFound(location='/', headers=headers)
