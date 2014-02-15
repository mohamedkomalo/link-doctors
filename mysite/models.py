from django.db import models
from linkedin import linkedin

# Create your views here.
class Doctor(models.Model):
  name=models.CharField(max_length=200)
  linked_id=models.CharField(max_length=200)
  
  @classmethod
  def create_from_token(cls, application):
    profile=application.get_profile(selectors=['id', 'first-name'])
    doctor = Doctor.objects.filter(linked_id=profile['id']).first()
    if doctor:
      return doctor
    
    doctor = Doctor() #TODO get linkedin id and info and put it in the model attributes
    doctor.linked_id=profile['id']
    doctor.name=profile['firstName']
    doctor.save()
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
  
  