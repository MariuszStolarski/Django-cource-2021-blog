from django.db import models

# Create your models here.

class Blog(models.Model):
    # blueprint of the model - database tables
    # requires to run migration comment to register the model:
    # python3 manage.py makemigrations
    # and then:
    # python3 manage.py migrate
    title = models.CharField(max_length=50)

