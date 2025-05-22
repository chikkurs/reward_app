from django.urls import path
from .views import user_register_view, user_login_view, user_home_view, user_logout_view,user_profile_view ,user_point_view, user_task_view, app_detail_view
urlpatterns = [
    path('register/', user_register_view, name='user_register'),
    path('login/', user_login_view, name='user_login'),
    path('logout/', user_logout_view, name='user_logout'),
    path('home/', user_home_view, name='user_home'),
    path('profile/', user_profile_view, name='user_profile'),
    path('point/', user_point_view, name='user_point'),
    path('task/', user_task_view, name='user_task'),
    path('app/<int:app_id>/', app_detail_view, name='app_detail'),
 
   

]
