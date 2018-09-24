from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, Base
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authn_policy = AuthTktAuthenticationPolicy('sosecret', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings, root_factory='pyramid_login.models.Root')
    config.include('pyramid_jinja2')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)    
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login','/login')
    config.add_route('logout','/logout')
    config.scan()
    return config.make_wsgi_app()
