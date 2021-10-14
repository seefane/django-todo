from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileForm, UpdateUserForm
from .models import Profile
from cloudinary.forms import cl_init_js_callbacks


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            messages.success(request, "{0}'s account was successfully registered".format(name))
            return redirect('todoHome')
    else:

        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    print(Profile.objects.filter(user=request.user)[0].image.url)
    return render(request, 'users/profile.html')


@login_required
def editProfile(request):

    curr_user = request.user
    if request.method == 'POST':
        upProfile = UserProfileForm(request.POST,request.FILES,instance=curr_user.profile)
        upUser = UpdateUserForm(request.POST,instance=curr_user)
        if upProfile.is_valid() and upUser.is_valid():
            upUser.save()
            upProfile.save()

            messages.success(request, "Information Updated")
            return redirect('editprofile')
    else:
        upProfile = UserProfileForm(instance=curr_user.profile)
        upUser = UpdateUserForm(instance=curr_user)
    context = {'upProfile': upProfile,
               'upUser': upUser}
    return render(request, 'users/editprofile.html', context)
