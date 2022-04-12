from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import List, Item
from .forms import NewList


# Create your views here.
def home(response):
    return render(response, "main/home.html")

def lists(response):
    all_ls = response.user.list.all()
    return render(response, "main/lists.html", {"lists": all_ls})

def items(response, id):
    items = Item.objects.filter(list_id =id)
    lst = List.objects.get(id = id)

    if not lst in response.user.list.all():
        return HttpResponseRedirect("/lists")

    context = {
        "items": items,
        "lst": lst,
    }

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in items:
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.completed = True
                else:
                    item.completed = False
                item.save()
        elif response.POST.get("addNewItem"):
            item = response.POST.get("newItem")

            if(len(item)) > 2:
                added = Item(name = item, completed = False, list= lst)
                added.save()


    return render(response, "main/items.html", context)

def create(response):
    if  response.method == "POST":
        form = NewList(response.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            d = List(name = name)
            d.save()
            response.user.list.add(d)
        
            return HttpResponseRedirect(reverse("items", args=[d.id]))

    form = NewList()
    return render(response, "main/create.html", {"form": form})