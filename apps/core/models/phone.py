from django.db import models


class Phone(models.Model):
    id=models.BigAutoField(primary_key=True)
    # Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Багато до одного
    client=models.ForeignKey("Client", on_delete=models.CASCADE, related_name="phones")