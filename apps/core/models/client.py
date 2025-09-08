import uuid

from django.db import models

from .account_coins import AccountCoins
# from apps.core.models.validators.validators import validate_not_future
from .validators.validators import validate_not_future


class Gender(models.IntegerChoices):
    NOT_SPECIFIED = 0, "Not specified"
    MALE = 1, "Male"
    FEMALE = 2, "Female"
    OTHER = 3, "Other"

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Звичайні поля
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    email = models.EmailField()
    birthday = models.DateField(validators=[validate_not_future])
    gender = models.IntegerField(choices=Gender.choices, default=Gender.NOT_SPECIFIED)
    photo = models.ImageField(upload_to="client_photos/", null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    # Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Зв'язки
    address = models.OneToOneField("Address", on_delete=models.SET_NULL, null=True, blank=True)
    accounts = models.ManyToManyField("AccountCoins", related_name="clients")
    # Методи
    def __str__(self):
        return (
            f"{self.id} "
            f"{self.surname} "
            f"{self.name} "
            f"{self.patronymic} "
            f"{self.email} "
            f"{self.birthday} "
            f"{self.gender} "
            f"{super().__str__()} "
        )

    class Meta:
        ordering = ["created_at"]
        # ordering = ["-created_at"]
        verbose_name = "Client"
        verbose_name_plural = "Clients"
