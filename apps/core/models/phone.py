from django.db import models


class Phone(models.Model):
    id=models.AutoField(primary_key=True)
    #Багато до одного
    client=models.ForeignKey("Client", on_delete=models.CASCADE, related_name="phones")