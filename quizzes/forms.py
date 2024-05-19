# pylint: disable=C0115
# pylint: disable=R0903

"""
Forms module for the quizzes application.

This module defines the following forms:
- QuizForm: Form for creating and editing Quiz instances.
- QuestionForm: Form for creating and editing Question instances.
- OptionForm: Form for creating and editing Option instances.

It also defines an inline formset for managing questions within a quiz.
"""

from django import forms
from django.forms import inlineformset_factory
from .models import Quiz, Question, Option


class QuizForm(forms.ModelForm):
    """
    Form for creating and editing Quiz instances.

    Meta:
        model (Quiz): The model this form is based on.
        fields (list): List of fields to include in the form.
        widgets (dict): Custom widgets for the form fields.
        labels (dict): Custom labels for the form fields.
    """

    class Meta:
        model = Quiz
        fields = ["title", "category", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }
        labels = {
            "title": "Название",
            "category": "Категория",
            "image": "Изображение",
            "change": "Заменить",
        }


class QuestionForm(forms.ModelForm):
    """
    Form for creating and editing Question instances.

    Meta:
        model (Question): The model this form is based on.
        fields (list): List of fields to include in the form.
        labels (dict): Custom labels for the form fields.
    """

    class Meta:
        model = Question
        fields = ["text", "question_type"]
        labels = {
            "text": "Текст вопроса",
            "question_type": "Тип вопроса",
        }


class OptionForm(forms.ModelForm):
    """
    Form for creating and editing Option instances.

    Meta:
        model (Option): The model this form is based on.
        fields (list): List of fields to include in the form.
        labels (dict): Custom labels for the form fields.
    """

    class Meta:
        model = Option
        fields = ["text", "is_correct"]
        labels = {
            "text": "Текст опции",
            "is_correct": "Правильный",
        }


# Inline formset for managing questions within a quiz
QuestionFormSet = inlineformset_factory(
    Quiz, Question, form=QuestionForm, extra=1, can_delete=True
)
