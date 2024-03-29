from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from core import views
from schedule import views as schedule_views
from userprofile import views as user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.social_login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),

    url(r'^signin/',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^core/',include('core.urls')),
    url(r'^user_logout/$', views.user_logout, name='logout'),

    url('register/', schedule_views.index, name='schedule'),
    path('select/', include('schedule.urls')),
    path('user/', include('userprofile.urls')),
]