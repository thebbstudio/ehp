from django.db import models


class Сategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    fullName = models.CharField(max_length=255)
    isMan = models.BooleanField(default=True) 
    birthDay = models.DateTimeField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    category = models.ForeignKey(Сategory, on_delete=models.CASCADE)
