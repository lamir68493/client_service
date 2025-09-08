from django.db import models


class News(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    #Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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