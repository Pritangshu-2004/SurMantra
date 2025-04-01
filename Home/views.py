from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('Header/navbar.html')
    return HttpResponse(template.render())
    
    # return render(request, 'index.html')
    
def about(request):
    # template = loader.get_template('Header/navbar.html')
    # return HttpResponse(template.render())
    return render(request, 'about.html')

def contact(request):
    # template = loader.get_template('Header/navbar.html')
    # return HttpResponse(template.render())
    return render(request, 'contact.html')