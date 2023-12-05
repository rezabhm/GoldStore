from django.urls import path
from . import views

urlpatterns = [

    path('send-code/phone-number=<str:phone_number>/', views.SendCode.as_view()),
    path('prove-auth-code/', views.ProveCode.as_view()),
    path('sign-up/', views.SignUp.as_view()),

]