from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    # login
    path('login', views.login_view, name='login_view'),
    # logout    
    # path('logout', views.logout_view, name='logout_view'),
    # registeration
    path('signup', views.signup_view, name='signup_view'),

]
