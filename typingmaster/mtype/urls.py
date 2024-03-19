from django.urls import path
from . import views

urlpatterns = [
        path('',views.index),
        path('login',views.login),
        path('register',views.register),
        path('typinglesson',views.typinglesson),
        path('typingtest',views.typingtest),
        path('game',views.game),
        path('into',views.into),
        path('profile',views.profile)
]
