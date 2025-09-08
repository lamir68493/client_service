from django.db import models


class AccountCoins(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    # Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Методи
    def __str__(self):
        return (
            f"{self.id} "
            f"{self.amount} "
            f"{super().__str__()} "
        )
