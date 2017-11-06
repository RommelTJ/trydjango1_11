from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view
def home(request):
    html_var = 'f strings'
    html = f"""
    <!DOCTYPE html>

    <head>

    </head>

    <body>
    <h1>Hello World</h1>
    <p>This is {html_var} coming through.</p>
    </body>

    </html>
    """
    # return render(request, "home.html", {})
    return HttpResponse(html)
