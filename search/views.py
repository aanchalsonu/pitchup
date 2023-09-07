from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SearchForm

def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            users = User.objects.filter(username__icontains=query)
            return render(request, 'search_results.html', {'users': users, 'query': query})
    else:
        form = SearchForm()

    return render(request, 'search_form.html', {'form': form})

def user_profile(request, username):
    user = User.objects.get(username=username)
    # Add logic to display user-specific information on the profile page
    return render(request, 'profile.html', {'user': user})
