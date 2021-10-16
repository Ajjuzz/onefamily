from django.db import models
from django.db.models.aggregates import Count


# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country
    

class State(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class District(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(State ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Register(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20)
    blood = models.CharField(max_length=5)
    phoneNo = models.CharField(max_length=12)
    country = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District ,on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=50)

class Contact(models.Model):

    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Message = models.TextField(max_length=500)

