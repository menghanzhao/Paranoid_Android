from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

#def search_result():