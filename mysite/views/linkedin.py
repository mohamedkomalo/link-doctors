from django.http import HttpResponseRedirect

from django.conf import settings
from mysite.models import Doctor

def login(request):


  url = request.build_absolute_uri("linkedin_login")
  # url goes back to request

  # create authentication class:
  authentication = linkedin.LinkedInDeveloperAuthentication(
    settings.CONSUMER_KEY, settings.CONSUMER_SECRET, 
    settings.USER_TOKEN, settings.USER_SECRET, url
    )

  # now its passed to the app:
  application = linkedin.LinkedInApplication(authentication)

  code = request.GET.get('code')

  if code:
    authentication.authorization_code = code
    token = authentication.get_access_token()
    # save in DB
    doctor = Doctor.create_from_token(token)
    
    return HttpResponseRedirect("/doctor/%s" % doctor.id)

  # if I dont have code, ask for another one
  return HttpResponseRedirect(authentication.authorization_url)


