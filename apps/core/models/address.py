from django.db import models


class Address(models.Model):
    id=models.AutoField(primary_key=True)
    #Зв'язки
    