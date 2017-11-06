import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view
def home(request):
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    num3 = random.randint(0, 100)
    some_list = [num1, num2, num3]
    context = {
        "html_var": "context variable",
       "num": num1,
        "some_list": some_list
    }
    return render(request, "base.html", context)
