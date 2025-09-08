from django.db import models


class Address(models.Model):
    id=models.BigAutoField(primary_key=True)
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=20)
    apartment = models.CharField(max_length=20)
    # Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Методи
    def __str__(self):
        return (
            f"{self.id} "
            f"{self.region} "
            f"{self.district} "
            f"{self.city} "
            f"{self.street} "
            f"{self.house} "
            f"{self.apartment} "
            f"{super().__str__()}"
        )
