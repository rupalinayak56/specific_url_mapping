from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def thallapathy(request):
    return HttpResponse("<h1><marquee>🎥The Hero Of Theri Movie is..🩷..Vijay Thallapthy..🤩..!!!Go watch and enjoy the 🍿..<marquee></h1>")
def heroine(request):
    return HttpResponse("<h1><marquee>And The Heroine is..🤩..Samantha Ruth Prabhu..🩷..!!!<marquee></h1>")