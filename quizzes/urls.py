from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_list, name="quiz_list")
]
