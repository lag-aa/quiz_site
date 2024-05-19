from django.shortcuts import render, redirect
from .models import Quiz, Category, Answer, Option


def quiz_list(request):
    quizzes = Quiz.objects.all()
    categories = Category.objects.all()
    context = {"quizzes": quizzes, "categories": categories}

    return render(request, "quizzes/quiz_list.html", context)


def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    return render(
        request, "quizzes/take_quiz.html", {"quiz": quiz, "questions": questions}
    )


def save_quiz_answers(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    if request.method == "POST":
        Answer.objects.filter(question__in=questions).delete()  # Clear previous answers
        for question in questions:
            if question.question_type == "TEXT":
                user_answer = request.POST.get(f"question_{question.id}")
                Answer.objects.create(question=question, text_answer=user_answer)
            elif question.question_type == "RADIO":
                selected_option_id = request.POST.get(f"question_{question.id}")
                if selected_option_id:
                    option = Option.objects.get(id=selected_option_id)
                    Answer.objects.create(question=question, selected_option=option)
            elif question.question_type == "CHECKBOX":
                selected_option_ids = request.POST.getlist(f"question_{question.id}")
                for option_id in selected_option_ids:
                    option = Option.objects.get(id=option_id)
                    Answer.objects.create(question=question, selected_option=option)
        return redirect("quiz_result", quiz_id=quiz.id)
    return redirect("take_quiz", quiz_id=quiz.id)


def quiz_result(request, quiz_id):
    pass