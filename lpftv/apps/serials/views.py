# Create your views here.

from django.http import HttpResponse

def show_serial(request):
     return HttpResponse("It's serial's page!")

