from django.db import models


class Phone(models.Model):
    id=models.BigAutoField(primary_key=True)
    phone=models.CharField(max_length=20)
    #Багато до одного
    client=models.ForeignKey("Client", on_delete=models.CASCADE, related_name="phones", null=True)
    # Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Методи
    def __str__(self):
        return (
            f"{self.id} "
            f"{self.phone} "
            f"{super().__str__()} "
        )
