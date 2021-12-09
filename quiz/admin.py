from django.contrib import admin
import nested_admin
from quiz.models import Answer, Categories, Questions, Quiz

# Register your models here.

class TocAnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    extra = 3
class TocQuestionInline(nested_admin.NestedStackedInline):
    model = Questions
    extra = 1
    inlines = [TocAnswerInline]
class TableOfQuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [TocQuestionInline]

admin.site.register(Quiz,TableOfQuizAdmin)
admin.site.register(Categories)
admin.site.register(Questions)
admin.site.register(Answer)