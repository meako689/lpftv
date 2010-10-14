# Create your views here.

from django.http import HttpResponse

def serial(request):
     return HttpResponse("It's serial's page!")

