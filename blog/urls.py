from django.urls import path
from .views.main_view import home, create_blog, edit_blog, single_blog
from .views.auth_view import register, loginUser

urlpatterns = [
    path("", home, name='home'),
    path("register/", register, name='register'),
    path("login/", loginUser, name='login'),
    path("create/",create_blog),
    path("single/", single_blog),
    path("edit/", edit_blog),
] 