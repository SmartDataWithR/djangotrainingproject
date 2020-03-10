from django.shortcuts import render, redirect
from .forms import EditUserForm, BasicProfileForm
from .models import BasicProfile

# Create your views here.
def edit_basic_profile(request):
    if request.method=='POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        user = User.objects.get(id=request.user.id) 
        print(user)
        basic_profile_form = BasicProfileForm(request.POST, instance=request.user)
        if user_form.is_valid() and basic_profile_form.is_valid():
            user_form.save()
            basic_profile_form.save()
            
            return redirect('home')
    else:
        user_form = EditUserForm(instance=request.user)
        basic_profile_form = BasicProfileForm(instance=request.user)
    context = {'user_form': user_form, 'basic_profile_form': basic_profile_form}
    return render(request, 'edit_basic_profile.html', context)

