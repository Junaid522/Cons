"""time_consultants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),

    path('login/', views.LoginView.as_view(), {'template_name': 'core/login.html'}, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),
    path('constructor/', include('constructor.urls')),
    path('api/', include('api.urls')),
    # path('institutes/', include('institutes.urls')),
    path('', include('home.urls')),
    path('celery-progress/', include('celery_progress.urls')),
    # re_path(r'^celery-progress/', include('celery_progress.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('summernote/', include('django_summernote.urls')),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
