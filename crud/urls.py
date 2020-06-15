from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/<int:contact_id>/', views.detail, name='detail')
]