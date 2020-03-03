from django.db import models



class Searchtitles(models.Model):
    title=models.CharField(max_length=100)