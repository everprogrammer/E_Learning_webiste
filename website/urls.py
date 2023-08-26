from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('contact', views.contact_view, name='contact_view'),
    path('test', views.test_view, name='test_view'),
    
]   