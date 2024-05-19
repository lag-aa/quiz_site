from django import forms
from .models import Quiz, Question, Option
from django.forms import inlineformset_factory


class QuizForm(forms.ModelForm):
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
    class Meta:
        model = Question
        fields = ["text", "question_type"]
        labels = {
            "text": "Текст вопроса",
            "question_type": "Тип вопроса",
        }


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ["text", "is_correct"]
        labels = {
            "text": "Текст опции",
            "is_correct": "Правильный",
        }


QuestionFormSet = inlineformset_factory(
    Quiz, Question, form=QuestionForm, extra=1, can_delete=True
)
