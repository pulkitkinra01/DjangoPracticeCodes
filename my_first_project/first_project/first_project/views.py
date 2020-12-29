from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        user_input = request.GET['user_input']
    return render(request, 'contact.html')
