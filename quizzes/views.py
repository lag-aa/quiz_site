from django.shortcuts import render
from .models import Quiz, Category


def quiz_list(request):
    quizzes = Quiz.objects.all()
    categories = Category.objects.all()
    context = {"quizzes": quizzes, "categories": categories}

    return render(request, "quizzes/quiz_list.html", context)
