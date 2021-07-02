from django.shortcuts import render

# view function for the "../" request
def starting_page(request):
    return render(request, "blog/index.html")


# view functionfor the "../posts" request
def posts(request):
    pass


# view functionfor the "../posts/a-slug-variable" request
def post_details(request):
    pass
