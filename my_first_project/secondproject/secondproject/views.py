from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

# def contact(request):
#     user_input = request.GET['user_input']
#     return render(request, 'contact.html', {'home_input', user_input})

def contact(request):

    user_input = request.GET['user_input']
    user_input = user_input.upper()
    # user_input = model.mulitplier(user_input)

    return render(request, 'contact.html', {'home_input':user_input})
