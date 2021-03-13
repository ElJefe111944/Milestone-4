from django.shortcuts import render


def profile(request):
    """ 
    A View to display the 
    User's profile page 
    """
    template = "profile/profile.html"
    context = {}
    return render(request, template, context)