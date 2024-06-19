from django.shortcuts import render
from .models import AboutPage  # Import your model if you need to fetch data

def about_view(request):
    """
    Renders the About page
    """
    about = AboutPage.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )