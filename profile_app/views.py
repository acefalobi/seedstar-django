from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from profile_app.forms import ProfileForm
from profile_app.models import Profile


def landing_page(request):
    return render(request, "landing_page.html")


def list_profile(request):
    profile = Profile.objects.all().order_by('-id')
    return render(request, "list.html", {'profiles': profile})


def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            is_saved = form.save()

            if is_saved:
                return HttpResponseRedirect('/list')
    else:
        form = ProfileForm()

    return render(request, "add.html", {'form': form})
