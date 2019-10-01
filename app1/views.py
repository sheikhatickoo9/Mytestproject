from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">code wid me</a></h1>')
def register(request):








    return render(request,"home.html")