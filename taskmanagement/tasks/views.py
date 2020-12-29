from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

class NewTaskForm( forms.Form ):
    task = forms.CharField( label="New Task" )
    # priority = forms.IntegerField( label="Priority", min_value=1, max_value=5)

#  Global variable can be accesible to everyone.
# tasks = ["foo", "bar", "kuchtohkar"]

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session["tasks"]
    })

def add(request):

    if request.method == "POST":
        form = NewTaskForm( request.POST ) # contains values which user submitted

        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]

            # HttpResponseRedirect is used to re-direct the reponse to different page.
            return HttpResponseRedirect( reverse("tasks:index") )
            # return render( request, 'tasks/index.html',{
            #     "tasks": tasks
            # })
        else:
            return render( request, 'tasks/add.html',{
                "form": form
            })

    return render(request, 'tasks/add.html',{
        "form" : NewTaskForm() # Creates a blank form
    })