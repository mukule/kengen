from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'adminstration/index.html')

def boardmembers(request):
    return render(request, 'adminstration/boardmembers.html')
