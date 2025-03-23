from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def BoolDiscovery(request):
    return render(request, 'book-discovery-call.html')