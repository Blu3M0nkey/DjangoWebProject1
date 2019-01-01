from django.shortcuts import render   # Added for this step
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "helloDjApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title': "Hello",
            'message':"some stuff happened on ",
            'content':  now.strftime("%A, %d %B, %Y at %X")
        }

    )

def about(request):
    return render(
        request,
        "helloDjApp/about.html",
        {
            'title' : "About HelloDjApp",
            'content' : "Example app page for Django."
        }
    )