from django.db import models


class Account(models.Model):
    id=models.AutoField(primary_key=True)
    amount=models.DecimalField(decimal_places=2, max_digits=20)
    #
