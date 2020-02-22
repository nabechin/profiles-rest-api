from django.urls import path
from profiles_api import views

urlpatterns = [
path('hello_views/',views.HelloApiView.as_view()),
]
