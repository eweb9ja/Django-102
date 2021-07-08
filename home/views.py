from django.shortcuts import render

def Home(request):
    
    text = "Hello World"
    
    Context = {
        "text" : text
    }
    return render(request, "home/index.html", Context)
