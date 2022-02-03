from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNote
from  django.contrib.auth.decorators import login_required



@login_required(login_url='/login')
def index(response, id):
    n = Note.objects.get(id=id)
    if n in response.user.note.all():
        return render(response, "main/index.html", {"n":n})
    else:
        return redirect("/")

@login_required(login_url='/login')
def home(response):
    return render(response, "main/home.html", {})


@login_required(login_url='/login')
def add(response):
    if response.method == "POST":
        form = AddNote(response.POST)
        if form.is_valid():
            t = form.cleaned_data["title"]
            txt = form.cleaned_data["text"]
            n = Note(title=t, text=txt)
            n.save()
            response.user.note.add(n)
        return redirect("/")
    else:
        form = AddNote()
    return render(response, "main/add.html", {"form":form})



@login_required(login_url='/login')
def update(response, id):
    note_to_update = Note.objects.get(id=id)
    #print(id)
    if response.method == "POST":
        form = AddNote(response.POST,instance=note_to_update)
        if form.is_valid():
            t = form.cleaned_data["title"]
            txt = form.cleaned_data["text"]
            note_to_update.title = t
            note_to_update.text = txt
            note_to_update.save()
            return redirect("/%i"%note_to_update.id)
    else:
        form = AddNote(instance=note_to_update)
    return render(response, "main/update.html", {"form": form})


@login_required(login_url='/login')
def delete(response, id):
    if response.method == "POST":
        n = Note.objects.get(id=id)
        n.delete()
        return redirect("/")
    return render(response, "main/delete.html", {})

def search(response):
    if response.method == "GET":
        query = response.GET
        current_user = response.user
        notes = current_user.note.all()
        context = {'notes':notes, 'query':query}
    return render(response, "main/search.html", context)