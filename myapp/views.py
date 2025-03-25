from urllib import request
from django.shortcuts import redirect, render

from myapp.models import Biodata

# Create your views here.

def index(request):
    return render(request, 'index.html')

def BoolDiscovery(request):
    return render(request, 'book-discovery-call.html')

def BookDiscoveryForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        docs = request.POST.get('docs')
        gender = request.POST.get('gender')
        region = request.POST.get('region')
        program = request.POST.get('program')

        user_form = Biodata(name=name, email=email, phone=phone, docs=docs, gender=gender, region=region, program=program )
        user_form.save()
        return redirect('submitbioform')
    return render(request, 'get-in-touch-form.html')

def submitBioForm(request):
    return render(request, 'submitedform.html')