"""
Admin module for managing the Category, Quiz, Question, \
and Option models in the Django admin interface.
"""

from django.contrib import admin
from .models import Category, Quiz, Question, Option


class OptionInline(admin.TabularInline):
    """
    Inline admin descriptor for Option model.
    Defines the formset for the Option model to be displayed inline within the Question admin view.
    """

    model = Option
    extra = 1


class QuestionInline(admin.TabularInline):
    """
    Inline admin descriptor for Question model.
    Defines the formset for the Question model to be displayed inline within the Quiz admin view.
    """

    model = Question
    extra = 5


class QuizAdmin(admin.ModelAdmin):
    """
    Admin view for the Quiz model.
    Displays the QuestionInline formset within the Quiz admin view.
    """

    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    """
    Admin view for the Question model.
    Displays the OptionInline formset within the Question admin view.
    Filters the questions by the associated quiz.
    """

    inlines = [OptionInline]
    list_filter = ["quiz"]


# Registering the models to the Django admin site
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
