"""djangopro URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),

    path('studentsignup',views.studentsignup,name="studentsignup"),
    path('teachersignup',views.teachersignup,name="teachersignup"),

    path('login',views.user_login,name="user_login"),
    path('logout',views.user_logout,name="user_logout"),

    path('upload',views.uploadbook,name='uploadbook'),
    path('books',views.uploadview,name='uploadview'),

    path('deletebook/<int:pk>',views.delete_book,name='delete_book'),
    path('viewbook/<int:pk>',views.view_book,name='view_book'),
    path('editbook/<int:pk>',views.edit_book,name='edit_book'),

    path('options',views.options,name='options'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

