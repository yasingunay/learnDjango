from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return render(request, "hello/index.html")

def yasin(request):
   return HttpResponse("Hello Yasin!")


def greet(request, name):
   return HttpResponse(f"Hello ,{name.capitalize()}")


def greet2(request,name):
   return render(request, "hello/greet.html", {"name": name.capitalize()})