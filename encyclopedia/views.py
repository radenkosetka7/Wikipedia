import markdown
import secrets
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util



class NewItemForm(forms.Form):
    title = forms.CharField(label="Title")
    content=forms.CharField(label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def add(request):

    if request.method == "POST":
        form=NewItemForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            if util.get_entry(title) is None:
                content=form.cleaned_data["content"]
                util.save_entry(title, "#" + title + "\n\n" + content)
                return HttpResponseRedirect(reverse("index"))
            else:
                 return render(request,"encyclopedia/existserror.html", {
                    "title":title
                 })
        else:
            return render(request, "encyclopedia/newPage.html", {
        "form":NewItemForm()
            })
    else: 
        return render(request, "encyclopedia/newPage.html", {
        "form":NewItemForm()
    })


def getClickedItem(request,title):
    if util.get_entry(title) is None:
        return render(request,"encyclopedia/notexistserror.html", {
            "form": title,
            "title":title
        })
    else:
        return render(request,"encyclopedia/data.html",{
             "title":title,
             "desc":markdown.markdown(util.get_entry(title))
        })

def random(request):
    title = secrets.choice(util.list_entries())
    return render(request,"encyclopedia/data.html",{
        "title":title,
        "desc":markdown.markdown(util.get_entry(title))
    })


