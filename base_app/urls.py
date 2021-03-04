from django.urls import path
from . import views

# Template URLS

app_name = "base_app"

urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/',views.user_login, name='user_login'),

]
