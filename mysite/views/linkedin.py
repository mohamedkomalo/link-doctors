def login(request):

  # defining authentication parameters:
  CONSUMER_KEY = "75ylhmbcn06a14"
  CONSUMER_SECRET = "tjEBRScvRSTRaKKH"
  USER_TOKEN = "27d39247-596b-49fd-8702-dfb6984ea420"
  USER_SECRET = "3b7ff8d5-21e0-4532-b261-041d23ed8363"

  # create authentication class:
  authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, USER_TOKEN, USER_SECRET, URL)

  # now its passed to the app:
  application = linkedin.LinkedInApplication(authentication)

  # now I can use "application" to get whatever I want from the file, this will bring back the whole profile:
  application.get_profile()

