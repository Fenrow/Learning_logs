from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    """the class responsible for the single exam"""
    text = models.CharField(max_length=200) #title
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Question(models.Model):
    """the class responsible for a single question in exam"""
    topic = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    """the class responsible for answering the question"""
    topic = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
