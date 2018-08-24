from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import nltk

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def caps(request):
    inputtext = request.POST['inputtext']
    
    return HttpResponse(inputtext)

