from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Category, Answer, Option
from .forms import QuizForm, QuestionFormSet


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
    quiz = Quiz.objects.get(id=quiz_id)
    answers = Answer.objects.filter(question__quiz=quiz)
    score = 0
    total_questions = quiz.questions.count()
    results = []

    for question in quiz.questions.all():
        question_result = {
            "question": question,
            "correct": [],
            "selected": [],
            "options": [],
        }
        if question.question_type == "TEXT":
            correct_option = question.options.filter(is_correct=True).first()
            user_answer = answers.filter(question=question).first()
            question_result["correct"].append(
                correct_option.text if correct_option else ""
            )
            question_result["selected"].append(
                user_answer.text_answer if user_answer else ""
            )
            if (
                user_answer
                and correct_option
                and user_answer.text_answer.strip().lower()
                == correct_option.text.strip().lower()
            ):
                score += 1
        else:
            correct_options = question.options.filter(is_correct=True)
            user_answers = answers.filter(question=question)
            selected_option_ids = user_answers.values_list("selected_option", flat=True)
            for option in question.options.all():
                question_result["options"].append(option)
                if option.is_correct:
                    question_result["correct"].append(option.text)
                if option.id in selected_option_ids:
                    question_result["selected"].append(option.text)
            if set(selected_option_ids) == set(
                correct_options.values_list("id", flat=True)
            ):
                score += 1
        results.append(question_result)

    return render(
        request,
        "quizzes/quiz_result.html",
        {
            "score": score,
            "quiz": quiz,
            "total_questions": total_questions,
            "results": results,
        },
    )


def manage_quiz(request):
    quizzes = Quiz.objects.all()
    return render(request, "quizzes/manage_quiz.html", {"quizzes": quizzes})


def create_quiz(request):
    if request.method == "POST":
        quiz_form = QuizForm(request.POST, request.FILES)
        question_formset = QuestionFormSet(
            request.POST, request.FILES, prefix="questions"
        )

        if quiz_form.is_valid() and question_formset.is_valid():
            quiz = quiz_form.save()
            questions = question_formset.save(commit=False)
            for question in questions:
                question.quiz = quiz
                question.save()
            return redirect("manage_quiz")
    else:
        quiz_form = QuizForm()
        question_formset = QuestionFormSet(prefix="questions")

    return render(
        request,
        "quizzes/create_quiz.html",
        {
            "quiz_form": quiz_form,
            "question_formset": question_formset,
        },
    )


def edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == "POST":
        quiz_form = QuizForm(request.POST, request.FILES, instance=quiz)
        question_formset = QuestionFormSet(request.POST, instance=quiz)

        if quiz_form.is_valid() and question_formset.is_valid():
            quiz = quiz_form.save()
            questions = question_formset.save(commit=False)
            for question in questions:
                question.quiz = quiz
                question.save()
            return redirect("manage_quiz")
    else:
        quiz_form = QuizForm(instance=quiz)
        question_formset = QuestionFormSet(instance=quiz)

    return render(
        request,
        "quizzes/edit_quiz.html",
        {
            "quiz_form": quiz_form,
            "question_formset": question_formset,
        },
    )


def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        quiz.delete()
        return redirect("manage_quiz")
    return render(request, "quizzes/delete_quiz.html", {"quiz": quiz})
