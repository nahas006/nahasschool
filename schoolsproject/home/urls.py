from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('your_view/<str:department_name>/', views.your_view, name='your_view'),
    path('logout',views.logout,name='logout'),

]