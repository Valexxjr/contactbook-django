from django.urls import path

from . import views
from .views import delete_contact, delete_phone, delete_attachment, delete_group

app_name = 'crud'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('groups', views.GroupList.as_view(), name='group_list'),
    path('groups/<int:pk>/update', views.GroupUpdate.as_view(), name='group_update'),
    path('groups/<int:pk>/delete', delete_group, name='group_delete'),
    path('contacts/<int:pk>/', views.DetailView.as_view(), name='contact_detail'),
    path('contacts/<int:pk>/update', views.ContactUpdate.as_view(), name='contact_update'),
    path('contacts/<int:pk>/delete', delete_contact, name='contact_delete'),
    path('contacts/<int:contact_id>/phones/<int:pk>/update', views.PhoneUpdate.as_view(), name='phone_update'),
    path('contacts/<int:contact_id>/attachments/<int:pk>/update', views.AttachmentUpdate.as_view(), name='attachment_update'),
    path('contacts/<int:pk>/phones/create', views.PhoneCreate.as_view(), name='phone_create'),
    path('contacts/<int:pk>/attachments/create', views.AttachmentCreate.as_view(), name='attachment_create'),
    path('contacts/<int:contact_id>/phones/<int:pk>/delete', delete_phone, name='phone_delete'),
    path('contacts/<int:contact_id>/attachments/<int:pk>/delete', delete_attachment, name='attachment_delete'),
    path('groups/create', views.GroupCreate.as_view(), name='group_create'),
]
