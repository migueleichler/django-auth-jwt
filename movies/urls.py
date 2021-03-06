"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from core import views as core_views

url_movie = [
    url(r'^signup', core_views.CreateUserView.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^movie/$', core_views.ListMovieView.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/$', core_views.MovieByIdView.as_view()),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(url_movie)),
]
