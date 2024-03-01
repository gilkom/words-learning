from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    words_to_learn = models.IntegerField(default=0, null=True)
    repetition_types = models.IntegerField(default=0, null=True)

    def delete_user_tokens(sender, instance, **kwargs):
        Token.objects.filter(user=instance).delete()



class Word(models.Model):
    word_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example_sentence = models.TextField(null=True)

    def __str__(self):
        return self.word
    

class Learning(models.Model):
    learning_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    word_id = models.ForeignKey(Word, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    learning_date = models.DateField()
    result = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.word.word} - {self.date}"
    
'''    
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    word_id = models.ForeignKey(Word, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    review_date = models.DateField()
    result = models.IntegerField()
'''