from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Quiz(models.Model):
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
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
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
        return self.text


class Option(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(
        Option, on_delete=models.CASCADE, null=True, blank=True
    )
    text_answer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.question.text}"
