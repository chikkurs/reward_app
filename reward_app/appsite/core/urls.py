from django.urls import path
from .views import admin_login_view, admin_dashboard_view, admin_add_app_view, admin_logout_view, admin_delete_app_view, admin_edit_app_view
urlpatterns = [
    path('', admin_login_view, name='admin_login'),
    path('admin-dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('add-app/', admin_add_app_view, name='add_app'),
    path('admin-logout/', admin_logout_view, name='admin_logout'),
    path('delete-app/<int:app_id>/', admin_delete_app_view, name='delete_app'),
    path('edit-app/<int:app_id>/', admin_edit_app_view, name='edit_app'),

]
