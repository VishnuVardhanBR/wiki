from django.shortcuts import render
from . import util, forms
import random
import markdown2
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
form = forms.SearchForm()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form
    })

def entry(request, title):
    try:
        content = markdown2.markdown(util.get_entry(title))
    except:
        content = None
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content,
        "form": form
    })

def search(request):
    if(request.method == 'GET'):
        form = forms.SearchForm(request.GET)
        if(form.is_valid()):
            search = form.cleaned_data['search'].lower()
            entries = util.list_entries()
            if(search in [x.lower() for x in entries]):
                return entry(request, search)
            else:
                queryResults = [x for x in entries if search.lower() in x.lower()]
                return render(request, "encyclopedia/search.html", {
                    "search": search,
                    "queryResults": queryResults,
                })

def createNew(request):
    if request.method == "GET":
        return render(request, "encyclopedia/createnew.html")

    # If route accessed via POST (i.e. after submitting form)
    elif request.method == "POST":

        # Stores entry's name and content
        form = request.POST
        title = form['title']
        content = form['content']

        # Checks file does not already exist and renders result (success / fail)
        entries = util.list_entries()

        print(title)
        print(entries)

        for item in entries:
            if title.lower() == item.lower():
                return render(request, "encyclopedia/result.html", {
                    "message": "Error! New entry was NOT added."
                })

        util.save_entry(title, content)
        return render(request, "encyclopedia/result.html", {
            "message": "Success! New entry added."
        })

def edit(request, title):
    if request.method == "GET":

        content = util.get_entry(title)

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content,
        })
    elif request.method == "POST":
        form = request.POST
        title = form['title']
        content = form['content']
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("wiki:entry", kwargs={'title': title}))

def random_page(request):
    entries = util.list_entries()
    page = random.choice(entries)
    #return HttpResponse(page)
    return HttpResponseRedirect(reverse("wiki:entry", kwargs={'title': page}))
