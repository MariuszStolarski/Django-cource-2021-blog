from datetime import date

from django.shortcuts import render

damy_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "mountains.jpg",
        "author" : "Maks",
        "date" : date(2021,7,6),
        "title" : "Mountain Hiking",
        "excerpt" : "There is nothing like the views you get hiking on the montains.",
        "content" : "{{ lorem 5 b random }}"
    },
    {
        "slug" : "this-is-coding",
        "image" : "coding.jpg",
        "author" : "Maks",
        "date" : date(2021,6,2),
        "title" : "My Codding",
        "excerpt" : "There is nothing like codding.",
        "content" : "{% lorem 6 b random %}"
    },
    {
        "slug" : "this-is-wood",
        "image" : "woods.jpg",
        "author" : "Maks",
        "date" : date(2020,10,9),
        "title" : "My woods",
        "excerpt" : "Wood is the wood.",
        "content" : "{% lorem 4 b random %}"
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

# helper function for sorting
def get_date(post):
    return post.get("date")

# view function for the "../" request
def starting_page(request):
    soreted_posts = sorted(damy_posts, key=get_date)
    latest_posts = damy_posts[-3:] # takes only 3 latest items from the list
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })


# view functionfor the "../posts" request
def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : damy_posts
    })


# view functionfor the "../posts/a-slug-variable" request
def post_details(request, a_slug_variable):
    identify_post = next (post for post in damy_posts if post['slug']==a_slug_variable)
    return render(request, "blog/post-detail.html", {
        "post" : identify_post
    })
