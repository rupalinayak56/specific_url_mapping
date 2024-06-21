from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def songkong(request):
    return HttpResponse("<h1><marquee>..🤩..My Demon is the one of the best webseries of Song Kong(Jeong Gu-won)..🥰💙<marquee></h1>")
def heroine(request):
    return HttpResponse("<h1><marquee>..🤩..And the cutest heroine is Kim Yoo-jung(Do Do Hee)..🫰🏻💗<marquee></h1>")
