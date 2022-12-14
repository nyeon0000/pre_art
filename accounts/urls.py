from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('newinfo/', views.newinfo, name='newinfo'),
    path('mypage/', views.mypage, name = 'mypage'),
]