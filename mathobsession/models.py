from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from jwt_auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=25)
    image = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Sketch(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    content = models.TextField()
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    user = models.ForeignKey(User, related_name='exercises', on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='exercises')
    sketch = models.ForeignKey(Sketch, related_name='exercises', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} level {self.level}'

class Contactus(models.Model):
    full_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
