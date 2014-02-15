from django.http import HttpResponse
from django.http import Http404
from mysite.models import *
from django.template import RequestContext, loader

def index(request):
	return HttpResponse("Index Page")

def show_doctor(request, doctor_id):
  doctor=Doctor.objects.filter(id=doctor_id).first()

  if not doctor:
	  raise Http404

  template = loader.get_template('doctor.html')
  context = RequestContext(request, {
    'doctor': doctor,
  })
  
  return HttpResponse(template.render(context))

def publish_case(request):
  template = loader.get_template('publish_case.html')
  context = RequestContext(request)
  return HttpResponse(template.render(context))