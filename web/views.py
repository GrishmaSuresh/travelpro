from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from web.models import destination, post_blogs
from .forms import post_blogsForm
import requests
import folium
from geopy.geocoders import Nominatim


def home(request):
    return render(request, 'web/home.html')


def about(request):
    return render(request, 'web/about.html')


def destiny(request):
    destines = destination.objects.all()
    return render(request, 'web/destination.html', {'dest': destines})


def services(request):
    return render(request, 'web/services.html')


def gallery(request):
    return render(request, 'web/gallery.html')


def blogs(request):
    info_blogs = post_blogs.objects.all()
    return render(request, 'web/blogs.html', {'info': info_blogs})


def success(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print("user created")
        return render(request, 'web/home.html')
    else:
        return render(request, 'web/home.html')


def post(request):
    if request.user.is_authenticated:
        submitted = False
        if request.method == 'POST':
            form = post_blogsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/post?submitted=True')
        else:
            form = post_blogsForm()
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'web/post_blogs.html', {'form': form, 'submitted': submitted})
    else:
        messages.error(request, 'Login to post your blogs!')
        return redirect('/blogs')


def packages(request):
    if request.method == 'POST':
        place = request.POST['place']
        date = request.POST['date']
        members = request.POST['members']

        spots = get_tourist_spots("New York")

        place = "New York"  # Hardcoding the place for now to simplify debugging
        spots = get_tourist_spots(place)

        # Debugging statements
        print("API Response:", spots)
        print("Type of API Response:", type(spots))  # Should be list or dict, depending on your API

        # If spots is a list, check if it has content
        if isinstance(spots, list):
            print("Number of spots returned:", len(spots))
            for spot in spots:
                print("Spot:", spot)

        return render(request, 'web/tourist_spots.html', {
            'place': place,
            'spots': spots,
        })


def get_tourist_spots(place):
    url = f"https://example.com/api/tourist-spots?location={place}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)  # Print the data to check the structure
        return data
    else:
        print(f"Error: {response.status_code}")
        return []


def bill(request):
    return render(request, 'web/bill.html')
