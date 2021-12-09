from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name}'
class Quiz(models.Model):
    user_id = models.IntegerField(blank=True,null=True)
    title = models.CharField( max_length=70)
    category = models.ForeignKey("quiz.Categories", verbose_name=("categories"), on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'
class Questions(models.Model):
    question = models.TextField()
    quiz = models.ForeignKey("quiz.Quiz", verbose_name=("quiz"),related_name='questions', on_delete=models.CASCADE,blank=True,null=True)
    difficulty = models.IntegerField()
    def __str__(self):
        return f'{self.question}'
class Answer(models.Model):
    question = models.ForeignKey("quiz.Questions", verbose_name=("questions"),related_name='answers', on_delete=models.CASCADE,blank=True,null=True)
    text = models.CharField(max_length=80)
    is_right = models.BooleanField()
    
    def __str__(self):
        return f'answer of: ({self.question}) -- {self.text}, {self.is_right}'
    