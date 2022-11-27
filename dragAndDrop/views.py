from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Drop

def index(request):
    return render(request, 'dragAndDrop/index.html')

def upload_file(request):
    if request.method == 'POST':
        myFile = request.FILES.get('file')
        # records = Drop.objects.all()
        # records.delete()
        Drop.objects.create(image=myFile)
        return HttpResponse('')
    return JsonResponse({'post':'false'})

def clear_images(request):
    records = Drop.objects.all()
    records.delete()
    return HttpResponse('')

def display(request):
    drops = Drop.objects.all()
    context = {
        'drops': drops,
    }
    return render(request, 'dragAndDrop/display.html', context)

def display_clear(request):
    Drop.objects.all().delete()
    drops = Drop.objects.all()
    context = {
        'drops': drops,
    }
    return render(request, 'dragAndDrop/display.html', context)