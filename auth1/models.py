from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(models.Model):
    id=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)