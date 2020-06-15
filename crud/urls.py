from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('contacts/<int:contact_id>/', views.detail, name='detail')
# ]