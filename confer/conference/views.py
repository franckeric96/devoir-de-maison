from django.shortcuts import render

# Create your views here.
def speaker(request):
    
    data = {
        
    }
    
    return render(request, 'speakers.html', data)


def schedule(request):
    
    data = {
        
    }
    
    return render(request, 'schedule.html', data)


def ticket(request):
    
    data = {
        
    }
    
    return render(request, 'tickets.html', data)