from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Klasa odpowiedzialna za temat poznawany przez użytkownika"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Zwraca reprezentację modelu jako ciąg tekstowy"""
        return self.text

class Entry(models.Model):
    """Klasa definiująca tekst w dyskusji pod danym tematem"""
    topic = models.ForeignKey(Topic , on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Zwraca reprezentację modelu jako ciąg tekstowy"""
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text
