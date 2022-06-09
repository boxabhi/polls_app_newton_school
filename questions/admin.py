import re
from django.contrib import admin

# Register your models here.

from .models import Question , Answers


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text' , 'user' ]


@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text' ,'question_text' ,'counter' ]


    def question_text(self , obj):
        return obj.question.question_text



