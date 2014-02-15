from mysite.models import Doctor
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from linkedin import linkedin

def linkedin_login(request):

  # defining authentication parameters:
  API_KEY = "75ylhmbcn06a14"
  API_SECRET = "tjEBRScvRSTRaKKH"
  
  USER_TOKEN = "27d39247-596b-49fd-8702-dfb6984ea420"
  USER_SECRET = "3b7ff8d5-21e0-4532-b261-041d23ed8363"

  RETURN_URL = request.build_absolute_uri("linkedin_login")
  # url goes back to request

  # create authentication class:
  authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
  
  print(authentication)  

  # now its passed to the app:
  application = linkedin.LinkedInApplication(authentication)

  code = request.GET.get('code')

  if code:
    authentication.authorization_code = code
    token = authentication.get_access_token()
    # save in DB
    doctor = Doctor.create_from_token(application)
    user = User.objects.get(id=doctor.user_id)

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return HttpResponseRedirect("/doctor/%s" % doctor.id)

  # if I dont have code, ask for another one
  return HttpResponseRedirect(authentication.authorization_url)
