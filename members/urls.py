from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_member, name="login"),
    path("logout/", views.logout_member, name="logout"),
    path("register/", views.register_member, name="register"),
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>/", views.member_profile, name="member-profile"),
    path("account/", views.member_account, name="account"),
    path("edit-account/", views.edit_account, name="edit-account"),
    path("create-skill/", views.create_skill, name="create-skill"),
    path("update-skill/<str:pk>/", views.update_skill, name="update-skill"),
    path("delete-skill/<str:pk>/", views.delete_skill, name="delete-skill"),
    path("inbox/", views.inbox, name="inbox"),
    path("message/<str:pk>/", views.view_message, name="message"),
    path("create-message/<str:pk>/", views.create_message, name="create-message"),

]
