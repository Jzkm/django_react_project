from django.db import models
import random
import string

# Create your models here.

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if len(Person.objects.filter(code=code)) == 0:
            break
    return code

class Person(models.Model):
    code = models.CharField(max_length=8,default=generate_unique_code,unique=True)
    picture = models.ImageField(upload_to='frontend/static/images',default='frontend/static/images/default.png')
    rank = models.IntegerField(null=True, default=800)
    plec = models.CharField(max_length=2,default='',unique=False)# XX lub XY
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.CharField(max_length=20,default='guest',unique=False)

class Exhibition(models.Model):
    name = models.CharField(max_length=30,default='Twoja nazwa',unique=True)
    password = models.CharField(max_length=30,default='Tajne haslo',unique=False)
    added_at = models.DateTimeField(auto_now_add=True)
    ex_persons = models.ForeignKey(Person, on_delete=models.CASCADE)