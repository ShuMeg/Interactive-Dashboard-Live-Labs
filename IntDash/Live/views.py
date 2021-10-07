from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse


# Create your views here.
def room1_display(request):
    return render(request, 'room1.html')
    
def room2_display(request):
    return render(request, 'room2.html')

def requestroom(request):
    return render(request, 'room1.html')
    
def myajaxtestview(request):
    print(request.POST['text'])
    return HttpResponse(mqtt.data)
    


    