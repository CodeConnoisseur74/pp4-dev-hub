from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginMember, name="login"),
        path('logout/', views.logoutMember, name="logout"),
        path('register/', views.registerMember, name="register"),
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>/", views.memberProfile, name="member-profile"),
    #     path('account/', views.memberAccount, name="account"),
    #     path('edit-account/', views.editAccount, name="edit-account"),
    # path('create-skill/', views.createSkill, name="create-skill"),
    # path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    # path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
    #     path('inbox/', views.inbox, name="inbox"),
    #     path('message/<str:pk>/', views.viewMessage, name="message"),
    #     path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]
