from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/home.html")

def about_me(request):
    return render(request,"core/about_me.html")

def contact(request):
    return render(request,"core/contact.html")