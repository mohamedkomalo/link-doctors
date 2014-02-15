from django.db import models
from linkedin import linkedin

# Create your views here.
class Doctor(models.Model):
  name=models.CharField(max_length=200)
  linked_id=models.CharField(max_length=200)
  access_token=models.CharField(max_length=200)
  
  def create_from_token(token):
    doctor = Doctor() #TODO get linkedin id and info and put it in the model attributes
    doctor.access_token=token
    return doctor

  def __str__(self):
    return self.name

class Case(models.Model):
  doctor=models.ForeignKey(Doctor)
  name=models.CharField(max_length=200)
  problem=models.CharField(max_length=200)
  age=models.CharField(max_length=200)
  gendar=models.CharField(max_length=200)

  def __str__(self):
    return self.name
  
  