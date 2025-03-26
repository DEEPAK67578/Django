from django.db import models

class Dummy(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=4)
    
    @property
    def getDiscount(self):
        return '%.2f' %(float(self.price) * 0.8)