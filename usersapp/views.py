from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def indexhtml(request):
    if request.method == "POST":
        context={
            'msg':'POST'
        }
    else:
        context={
            'msg':'GET'
        }
    return render(request, 'index.html', context)