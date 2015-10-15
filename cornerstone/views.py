from django.shortcuts import render_to_response,render,HttpResponseRedirect
from .models import CornerstoneUserProfile
from .forms import CornerstoneUserProfileForm


def show_csod(request):
    if request.method == 'POST':
        form = CornerstoneUserProfileForm(request.POST, request.FILES)

        csvfile = request.FILES['csv_file']
        file = open(csvfile,'r+')
        reader = csv.reader(file)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cornestone.views.show_csod'))
    else:
        form = CornerstoneUserProfileForm()

    nodes = CornerstoneUserProfile.objects.all()
    return render(request, "base.html", {'form': form, 'nodes': nodes})
