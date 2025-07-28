from django.db import models


# practica con foreing key:
class Menu_category(models.Model):
    menu_category_name = models.CharField(max_length=200)



class Menu(models.Model):
    name=models.CharField(max_length=100)
    cuisine=models.CharField(max_length=100)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(
        Menu_category
        ,on_delete=models.PROTECT
        # , default=0
        ,null=True
        ,blank=True
        )



 