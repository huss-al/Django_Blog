from django.shortcuts import render
from .models import AboutPage  # Import your model if you need to fetch data
from .forms import CollaborateForm

def about_view(request):
    """
    Renders the About page
    """
    about = AboutPage.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
         },
    )