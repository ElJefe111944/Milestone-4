from django.shortcuts import render


def profile(request):
    """ 
    A View to display the 
    User's profile page 
    """
    template = "profiles/profile.html"
    context = {}
    return render(request, template, context)