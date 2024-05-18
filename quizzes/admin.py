from django.contrib import admin
from .models import Category
from .models import Quiz
from .models import Question
from .models import Option
from .models import Answer

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
