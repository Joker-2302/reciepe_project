from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1>hello there, this is my first project</h1>")
    people = [
        {"name":"Shubham", "age":28},
        {"name":"Deodhar", "age":23}
    ]
    return render(request, 'index.html', context={"page":"Home","people":people})

def about(request):
    context = {'page':'About'}
    return render(request, 'about.html', context)

def contact(request):
    context = {'page':'Contact'}
    return render(request, 'contact.html', context)


def success_page(request):
    return HttpResponse("<h1> This is success page </h1>")
# Create your views here.
