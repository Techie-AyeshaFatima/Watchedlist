from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from datetime import datetime
import json
import requests

from .models import User, Item

def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# default page
def index(request):
    return render(request, "watchedlist/index.html")

# login page
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "watchedlist/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "watchedlist/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# registration page
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "watchedlist/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "watchedlist/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "watchedlist/register.html")

def lookup(title):
    """Look up quote for searched."""
    url = f"http://www.omdbapi.com/?apikey=e2e63503&s={title.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP error responses
        return response.json()
    except requests.RequestException as e:
        print(f"Request error: {e}")
    except (KeyError, ValueError) as e:
        print(f"Data parsing error: {e}")
    return None

def search(request):
    # fetching the search page
    if request.method == "POST":
        searched = request.POST.get("searched")

        if not searched:
            return HttpResponse("must enter the searched", status=400)

        results = lookup(searched)

        if results is None or results.get("Response") == "False":
            return render(request, "watchedlist/results.html", {"message": "Sorry! Could not find results"})

        return render(request, "watchedlist/results.html", {"results": results["Search"]})

def item(request, id):
    """Look up details for a specific movie."""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"), {
                "message": "Passwords must match."})
    else:
        url = f"http://www.omdbapi.com/?apikey=e2e63503&i={id}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP error responses
            item = response.json()

            itemdata = Item.objects.filter(item_id=id, user=request.user).first()
            if not itemdata:
                # empty form
                return render(request, "watchedlist/item.html", {"item": item})
            else:   
                # prefilled form 
                return render(request, "watchedlist/item.html", {"item": item, "prefilled": True, "itemdata": itemdata})
        except requests.RequestException as e:
            print(f"Request error: {e}")
        except (KeyError, ValueError) as e:
            print(f"Data parsing error: {e}")
        return HttpResponse("Item not found.", status=404)

from django.contrib.auth.decorators import login_required
@login_required
def update_list(request, id):
    url = f"http://www.omdbapi.com/?apikey=e2e63503&i={id}"
    response = requests.get(url)
    response.raise_for_status()
    item = response.json()

    if request.method == "POST":
        itemdata = Item.objects.filter(item_id=id, user=request.user).first()
        if not itemdata:
            itemdata = Item(
                item_id=id,
                title=item['Title'],
                type=item['Type'],
                user=request.user,
                comment=request.POST.get("note", ""),
                rate=request.POST.get("rating", None),
                list=request.POST.get("btnradio", "watchlist"),
                image_url= item['Poster']
            )
        else:
            itemdata.comment = request.POST.get("note", "")
            itemdata.rate = request.POST.get("rating", itemdata.rate)
            itemdata.list = request.POST.get("btnradio", itemdata.list)
        itemdata.save()    
    return HttpResponseRedirect(reverse("mylist"))

# viewing the users item list
def mylist(request):
    if request.method == "GET":
        filter_type = request.GET.get('type')
        if filter_type:
            mylist = Item.objects.filter(user=request.user, type=filter_type)
        else:
            mylist = Item.objects.filter(user=request.user)
        return render(request, "watchedlist/mylist.html", {"mylist": mylist})
    else:
        return HttpResponse(status=405)  # Method not allowed

# viewing the users watch list
def watchlist(request):
    if request.method == "GET":
        filter_type = request.GET.get('type')
        if filter_type:
            watchlist = Item.objects.filter(user=request.user, list='watchlist', type=filter_type)
        else:
            watchlist = Item.objects.filter(user=request.user, list='watchlist')
        return render(request, "watchedlist/watchlist.html", {"watchlist": watchlist})
    else:
        return HttpResponse(status=405)  # Method not allowed

# viewing the users watched list
def watched(request):
    if request.method == "GET":
        filter_type = request.GET.get('type')
        if filter_type:
            watchedlist = Item.objects.filter(user=request.user, list='watchedlist', type=filter_type)
        else:
            watchedlist = Item.objects.filter(user=request.user, list='watchedlist')
        watchedlist = watchedlist.order_by('-rate')
        return render(request, "watchedlist/watchedlist.html", {"watchedlist": watchedlist})
    else:
        return HttpResponse(status=405) # Method not allowed

# viewing the users dropped list
def dropped(request):
    if request.method == "GET":
        filter_type = request.GET.get('type')
        if filter_type:
            droppedlist = Item.objects.filter(user=request.user, list='droppedlist', type=filter_type)
        else:
            droppedlist = Item.objects.filter(user=request.user, list='droppedlist')
        droppedlist = droppedlist.order_by('-rate')
        return render(request, "watchedlist/droppedlist.html", {"droppedlist": droppedlist})
    else:
        return HttpResponse(status=405)  # Method not allowed
