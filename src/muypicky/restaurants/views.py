import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view
def home(request):
    num = random.randint(0, 100)
    return render(request, "base.html", {"html_var": "context variable", "num": num})
