from django.db import models

class Menu(models.Model):
    name=models.CharField(max_length=100)
    cuisine=models.CharField(max_length=100)
    price=models.IntegerField()
    lastprice=models.IntegerField(default=0)


    def __str__(self):
        return self.name  + ' - ' + self.cuisine + ' - $' + str(self.price)  
    

    
#Ejemplo de formulario con ingreo a la db    
class Logger (models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models. CharField(max_length = 200)
    time_log = models.TimeField(help_text="Enter the exact time!")   