from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_list, name="quiz_list"),
    path("<int:quiz_id>/take/", views.take_quiz, name="take_quiz"),
    path("<int:quiz_id>/save/", views.save_quiz_answers, name="save_quiz_answers"),
    path("<int:quiz_id>/results/", views.quiz_result, name="quiz_result"),
]
