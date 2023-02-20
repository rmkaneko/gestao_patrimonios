from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length = 14)
    photo = models.ImageField(upload_to='clients_images', null=True, blank=True, height_field=None, width_field=None, max_length=100)
    
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name