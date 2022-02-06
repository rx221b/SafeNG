from django.db import models

# Create your models here.
class Search(models.Model):
        pub_date = models.DateTimeField('date published')
