from django.shortcuts import render

# Create your views here.
# example/views.py
from datetime import datetime

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, World!")


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Django Project!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)