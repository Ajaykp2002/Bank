from django.http import HttpResponse
from django.shortcuts import render

# Create your vi
def demo(request):
    return render(request,'index.html')