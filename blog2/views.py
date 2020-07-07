from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def insoo(request):
    return render(request,"insoo.html")

def jinsu(request):
    return render(request,"jinsu.html")