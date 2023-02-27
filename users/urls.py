from django.urls import path
from users import views
from rest_framework.authtoken import views as auth_token_views

urlpatterns = [
    # template urls
    path('register/', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    # api urls
    path("api/register/", views.RegisterView.as_view()),
    path('api/token/', auth_token_views.obtain_auth_token),
]
