from django.urls import path
from . import views

urlpatterns = [

    path('send-code/phone-number=<str:phone_number>/', views.SendCode.as_view())


]