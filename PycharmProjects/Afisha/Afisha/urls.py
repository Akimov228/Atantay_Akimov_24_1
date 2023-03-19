"""Afisha URL Configuration

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
from django.urls import path
from . import swagger

from movie_app.views import ReviewDetailAPIView, ReviewListAPIView, MovieReviewListAPIView, MovieListAPIView, MovieDetailAPIView, \
    DirectorListCreateAPIView, DirectorDetailAPIView

from users.views import RegistrationUserAPIView, UserAuthorizationAPIView, UserConfirmationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', DirectorListCreateAPIView.as_view()),
    path('api/v1/directors/<int:pk>/', DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', MovieListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('api/v1/movies/reviews/', MovieReviewListAPIView.as_view()),
    path('api/v1/users/registration/', RegistrationUserAPIView.as_view()),
    path('api/v1/users/confirm/', UserConfirmationAPIView.as_view()),
    path('api/v1/users/authorization/', UserAuthorizationAPIView.as_view())
]

urlpatterns += swagger.urlpatterns