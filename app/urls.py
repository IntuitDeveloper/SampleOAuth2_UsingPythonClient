from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

app_name = 'app'

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^oauth/?$', views.oauth, name='oauth'),
    url(r'^openid/?$', views.openid, name='openid'),
    url(r'^callback/?$', views.callback, name='callback'),
    url(r'^connected/?$', views.connected, name='connected'),
    url(r'^qbo_request/?$', views.qbo_request, name='qbo_request'),
    url(r'^revoke/?$', views.revoke, name='revoke'),
    url(r'^refresh/?$', views.refresh, name='refresh'),
    url(r'^user_info/?$', views.user_info, name='user_info'),
    url(r'^migration/?$', views.migration, name='migration'),
]
