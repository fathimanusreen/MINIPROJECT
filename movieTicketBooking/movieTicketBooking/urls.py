"""movieTicketBooking URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view
from django.contrib.auth import views as auth_view
from user import views


urlpatterns = [
    path('',auth_view.LoginView.as_view(template_name='user/login.html'),name='user-login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='user/logout.html'),name='user-logout'),
    path("admin/", admin.site.urls),
    path('register/',user_view.register , name="user-register"),
    path('dashboard/',views.dashboard,name="dashbaord-index"),
    path('customer/', include('customer.urls')),
    path('theare/', include('theatre.urls')),
    path('movieadministrator/', include('movieadministrator.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
