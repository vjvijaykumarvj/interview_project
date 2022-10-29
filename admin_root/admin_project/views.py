from django.shortcuts import render,HttpResponse


def Home(request):
    return render(request,'home.html')