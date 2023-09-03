from django.urls import path
from . import views
from .models import Contact

app_name = 'website'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('test', views.test_view, name='test_view'),
    path('newsletter/', views.newsletter_view, name='newsletter_view'),
]   