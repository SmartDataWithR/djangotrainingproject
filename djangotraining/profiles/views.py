from django.shortcuts import render
from .forms import EditBasicProfileForm

# Create your views here.
def edit_basic_profile(request):
    if request.method=='POST':
        form = EditBasicProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Dein Konto wurde bearbeitet.'))
            return redirect('home')
    else:
        form = EditBasicProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'edit_basic_profile.html', context)