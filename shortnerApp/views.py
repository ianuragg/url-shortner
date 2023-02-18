from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Shortner
import string
import random


def home(request):
    get_link = ""
    if request.method == "POST":
        url = request.POST['url-shortner']
        #Generating random short text
        lower_alpha = string.ascii_lowercase
        upper_alpha = string.ascii_uppercase
        digits = string.digits
        few_char = "-_"

        random_list = []
        random_list.extend(list(lower_alpha))
        random_list.extend(list(upper_alpha))
        random_list.extend(list(digits))
        random_list.extend(list(few_char))

        random.shuffle(random_list)
        slug = "".join(random.sample(random_list, 6))

        new_link = Shortner(url=url, slug=slug, is_active=True)
        new_link.save()

        get_link = Shortner.objects.filter(id=new_link.id)
        messages.success(request, "Link Generated.")

    
    return render(request, "home.html", {"urlData":get_link})

def shortenUrl(request, slug):
    if request.method == "GET":
        get_link = Shortner.objects.get(slug=slug)
        
        return redirect(get_link.url)