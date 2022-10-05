from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.landing_page, name="landing_page"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('detail/<str:usrn>/', views.userDetail, name="details"),
    path('finder/', views.finderPage, name='univ_finder'),
    path('univDetail/', views.univDetailPage, name='univ_detail'),
    path('donatePay/', views.donatePay, name='donate_pay'),
    path('donate/', views.donate, name='donate'),
    path('delete/', views.deleteUser, name='delete_user'),
]
