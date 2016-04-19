from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^dashboard/', views.login, name='login'),
    
]