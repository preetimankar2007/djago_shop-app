from django.http import HttpResponse
from django.shortcuts import render
from .models import Blogpost
# Create your views here.
def index(request):
    # blogs= Blogpost.objects.all()

    return render(request, "blog/index.html",)

def blogpost(request,id):
    blogpost = Blogpost.objects.filter(id=id)[0]
    print(blogpost)
    return render(request, "blog/blogpost.html")