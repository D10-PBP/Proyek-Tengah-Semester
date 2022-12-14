from django.urls import path
from fitur_autentikasi.views import *

app_name = 'fitur_autentikasi'

urlpatterns = [
    path('register/', register, name='register'),
    path('register/ajax', register_ajax, name='register_ajax'),
    path('login/', login_user, name='login'),
    path('login/ajax', login_ajax, name='login_ajax'),
    path('logout/', logout_user, name='logout'),
    path('logout/ajax', logout_ajax, name='logout_ajax'),
    path('profile/<str:username>', show_profile, name='show_profile'),
    path('user-data/<str:username>', get_user_data, name='get_user_data'),
    path('update-user-data/<str:username>', update_user_data, name='update_user_data'),
]