from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import User,Auction_listings,Category,Watchlist


def index(request):
    listings=Auction_listings.objects.filter(is_active=True)
    categories=Category.objects.all()
    return render(request, "auctions/index.html",{
        "listings":listings,
        "categories":categories,
        "heading":"Active Listing"
    })


def login_view(request):
    categories=Category.objects.all()
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password.",
                "categories":categories
            })
    else:
        return render(request, "auctions/login.html",{
            "categories":categories
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    categories=Category.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match.",
                "categories":categories
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken.",
                "categories":categories
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
def create(request):
    owner=request.user
    if request.method=="GET":
        return render(request,"auctions/create.html",{
            "owner":owner,
            "cars":Category.objects.all(),
            "categories":Category.objects.all()
        })
    else:
        title=request.POST['title']
        description=request.POST['description']
        imgurl=request.POST['imgurl']
        stbid=request.POST['stbid']
        category=request.POST['category']
        category_instance = get_object_or_404(Category, name=category)
        newlisting=Auction_listings(title=title, Owner=owner, description=description, imgurl=imgurl, startingbid=stbid, category=category_instance )
        newlisting.save()
        return HttpResponseRedirect(reverse("index"))
    
def listing_detail(request,listing_id):
    listing=Auction_listings.objects.get(id=listing_id)
    T_F=request.user = Watchlist.user
    if request.method=="GET":
        return render(request, "auctions/listing_detail.html",{
        "listing":listing,
        "categories":Category.objects.all(),
        "T_F":T_F
        })
    else:
        user=request.user
        listing_instance=Auction_listings.objects.get(id=listing_id)
        watchlist_item=Watchlist(user=user,listing=listing_instance)
        watchlist_item.save()
        return HttpResponseRedirect(reverse("index"))



def categories(request):
    categories=Category.objects.all()
    return render(request, "auctions/category.html",{
        "categories": categories,
    })

def category_name(request,category_name):
    category = get_object_or_404(Category, name=category_name)
    listing=Auction_listings.objects.filter(category=category, is_active=True)
    heading=f'Active listings of {category.name} cars'
    return render(request, "auctions/index.html",{
        "listings":listing,
        "categories":category,
        "heading":heading
    })
    
