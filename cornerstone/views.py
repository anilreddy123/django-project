from django.shortcuts import render_to_response,render
from .models import CornerstoneUserProfile
from .forms import CornerstoneUserProfileForm



def show_csod(request):
    manager_data = []
    if request.method == 'POST':
      form = CornerstoneUserProfileForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request, "base.html", {'form': form,})
    else:
       form = CornerstoneUserProfileForm()

    nodes = CornerstoneUserProfile.objects.all()
    print "Count"
    count = CornerstoneUserProfile.objects.count()
    for id in range(0, count):
        users = CornerstoneUserProfile.objects.filter(parent_id = id).exclude(User_ID__isnull = True)
        if users:
            users_manager = CornerstoneUserProfile.objects.filter(id = id).exclude(User_ID_isnull = True)
            for manager in users_manager:
                if manager.User_ID in manager_data:
                    print "maanager data"
                    print  manager.User_ID
                    for user_info in users:
                        print user_info.User_ID, user_info.parent_ID

    return render(request, "base.html", {'form': form, 'nodes': nodes, 'count': count})



