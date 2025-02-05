from django.urls import path
from .views.main_view import home, create_blog, edit_blog, single_blog, delete_blog
from .views.auth_view import register, loginUser

urlpatterns = [
    path("", home, name='home'),
    path("register/", register, name='register'),
    path("login/", loginUser, name='login'),
    path("create/",create_blog),
    path("<int:blog_id>", single_blog),
    path("edit/", edit_blog),
    path("<int:blog_id>/delete", delete_blog, name="delete_blog")
] 