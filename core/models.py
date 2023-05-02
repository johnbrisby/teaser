from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    text = models.TextField(blank=True,null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '姓名:'+self.name+'   '+'手机号:'+self.phone