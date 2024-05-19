"""
App configuration module for the quizzes application.

This module defines the QuizzesConfig class which configures the 'quizzes' application.
"""

from django.apps import AppConfig


class QuizzesConfig(AppConfig):
    """
    Configuration class for the 'quizzes' application.

    Attributes:
        default_auto_field (str): The default field type for auto-generated primary keys.
        name (str): The name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "quizzes"
