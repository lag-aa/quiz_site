"""
URL configuration module for the quizzes application.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_list, name="quiz_list"),
    path("manage/", views.manage_quiz, name="manage_quiz"),
    path("create/", views.create_quiz, name="create_quiz"),
    path("<int:quiz_id>/edit/", views.edit_quiz, name="edit_quiz"),
    path("<int:quiz_id>/delete/", views.delete_quiz, name="delete_quiz"),
    path("<int:quiz_id>/take/", views.take_quiz, name="take_quiz"),
    path("<int:quiz_id>/save/", views.save_quiz_answers, name="save_quiz_answers"),
    path("<int:quiz_id>/results/", views.quiz_result, name="quiz_result"),
]
