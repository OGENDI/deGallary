from encodings import search_function
from django.shortcuts import render
from urllib import response
from email import message
import datetime as dt
from .models import Image


# Create your views here.
def home(request):
    date = dt.date.today()
    return render(request,'index.html',{"date": date})

def photos(request):
    my_gallery = Image.get_images()
    print(my_gallery)
    return render(request,'gallery.html',{"gallery":my_gallery})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_name = request.GET.get('category')
        search_images = Image.search_image_by_cat(search_name)

        print(search_name)

        user_msg = f'{search_name}'
        return render(request, 'search.html', {'message':user_msg, 'images':search_images})

    else:
        messages = "Please search again."
        return render(request, 'search.html', {'message':messages})

def about(request):
    title = "About Me"
    return render(request,'about.html',{'aboutMe':title})

def contact(request):
    title = "Contact Me"
    return render(request, 'contact.html',{'contact':title})

