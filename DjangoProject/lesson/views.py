
from django.http import HttpResponse


# Create your views here.

def lesson(request):
    return HttpResponse('hello Django')

