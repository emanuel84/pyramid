from pyramid.view import view_config
from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPFound
from .models import DBSession, User

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    if request.authenticated_userid:
        user = DBSession.query(User).filter_by(username=request.authenticated_userid).one_or_none()     
        return {'user': user}
    headers = forget(request)
    return HTTPFound(location='/login', headers=headers)    

@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    if request.method == 'POST':
        username = request.params.get('login')        
        password = request.params.get('password')   
        user = DBSession.query(User).filter_by(username=username).one_or_none()     
        if user and user.password == password:
            headers = remember(request, username)
            return HTTPFound('/', headers=headers)
    return {}    

@view_config(route_name='logout', renderer='templates/logout.jinja2')
def logout(request):
    headers = forget(request)
    return HTTPFound(location='/', headers=headers)
