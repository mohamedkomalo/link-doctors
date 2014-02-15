from main.models import *

d = Doctor.objects.get(pk=1)
c = Case.objects.get(pk=1)
c.doctor