"""
Models module for the quizzes application.

This module defines the following models:
- Category: Represents a category of quizzes.
- Quiz: Represents a quiz belonging to a category.
- Question: Represents a question within a quiz.
- Option: Represents an option for a question.
- Answer: Represents an answer to a question.
"""

from django.db import models


class Category(models.Model):
    """
    Represents a category of quizzes.

    Attributes:
        name (str): The name of the category.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    # pylint: disable=C0115
    # pylint: disable=R0903
    class Meta:
        verbose_name_plural = "Categories"


class Quiz(models.Model):
    """
    Represents a quiz belonging to a category.

    Attributes:
        title (str): The title of the quiz.
        category (Category): The category the quiz belongs to.
        image (ImageField): An optional image for the quiz.
    """

    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="quizzes",
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="quiz_images/", blank=True, null=True)

    def __str__(self):
        return str(self.title)

    # pylint: disable=C0115
    # pylint: disable=R0903
    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    """
    Represents a question within a quiz.

    Attributes:
        quiz (Quiz): The quiz the question belongs to.
        text (str): The text of the question.
        question_type (str): The type of the question (e.g., text, radio button, checkbox).
    """

    QUESTION_TYPES = [
        ("TEXT", "Text"),
        ("RADIO", "Radio Button"),
        ("CHECKBOX", "Checkbox"),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=200)
    question_type = models.CharField(
        max_length=8, choices=QUESTION_TYPES, default="TEXT"
    )

    def __str__(self):
        return str(self.text)


class Option(models.Model):
    """
    Represents an option for a question.

    Attributes:
        question (Question): The question the option belongs to.
        text (str): The text of the option.
        is_correct (bool): Indicates whether the option is correct.
    """

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)


class Answer(models.Model):
    """
    Represents an answer to a question.

    Attributes:
        question (Question): The question being answered.
        selected_option (Option): The selected option for the question (if applicable).
        text_answer (str): The text answer for the question (if applicable).
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(
        Option, on_delete=models.CASCADE, null=True, blank=True
    )
    text_answer = models.CharField(max_length=200, blank=True)

    # pylint: disable=E1101
    def __str__(self):
        return str(self.question.text)
