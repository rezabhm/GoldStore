"""GoldStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Gold Store API')

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", schema_view),

    # API
    path("Home/", include('API.Home.urls')),
    path("Authentication/", include('API.Authentication.urls')),

    path("UserDashboard-DeskPage/", include('API.UserDashboard_DeskPage.urls')),
    path("UserDashboard-GetRequest/", include('API.UserDashboard_GetRequest.urls')),
    path("UserDashboard-GoldBuySale/", include('API.UserDashboard_GoldBuySale.urls')),
    path("UserDashboard-UserReporting/", include('API.UserDashboard_UserReporting.urls')),

    path("AdminDashboard-DeskPage/", include('API.AdminDashboard_DeskPage.urls')),
    path("AdminDashboard-GetRequest/", include('API.AdminDashboard_GetRequest.urls')),
    path("AdminDashboard-Transaction/", include('API.AdminDashboard_Transaction.urls')),
    path("AdminDashboard-Setting/", include('API.AdminDashboard_Setting.urls')),
    path("AdminDashboard-BuySale/", include('API.AdminDashboard_BuySale.urls')),

]
