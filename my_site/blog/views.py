from django.shortcuts import render

# view function for the "../" request
def starting_page(request):
    return render(request, "blog/index.html")


# view functionfor the "../posts" request
def posts(request):
    return render(request, "blog/all-posts.html")


# view functionfor the "../posts/a-slug-variable" request
def post_details(request, a_slug_variable):
    return render(request, "blog/post-detail.html")
