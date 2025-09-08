from django.db import models


class News(models.Model):
    id=models.BigAutoField(primary_key=True)
    #Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
