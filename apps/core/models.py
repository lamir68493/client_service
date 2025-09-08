from django.db import models
'''
# Create your models here.
class Sample(models.Model):
    #ID
    id = models.AutoField(primary_key=True)
    id = models.BigAutoField(primary_key=True)
    id = models.SmallAutoField(primary_key=True)
    #Звичайні поля
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.IntegerField(choices=Gender.choices)
    #Метадані
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Зв'язки
    # client = models.OneToOneField("Client", on_delete=models.CASCADE)
    #Налаштування
    class Meta:
        verbose_name = "Sample"
        verbose_name_plural = "Samples"
    #Стандартні Методи
    #Методи
'''
