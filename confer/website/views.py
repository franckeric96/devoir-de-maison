from django.shortcuts import render

# Create your views here.

def home(request):
    
    data = {
        
    }
    return render(request, 'index.html', data)


def about(request):
    
    data = {
        
    }
    
    return render(request, 'about.html', data)


def contact(request):
    
    data = {
        
    }
    
    return render(request, 'contact.html', data)