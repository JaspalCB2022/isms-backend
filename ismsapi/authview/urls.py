from django.urls import path

from . import views

urlpatterns = [
  # path('authlogin/', views.UserLoginView.as_view()),
  # path('authlogin/<int:id>/', views.UserLoginView.as_view()),
  path('login/', views.UserLogin.as_view(), name='user-login'),
]