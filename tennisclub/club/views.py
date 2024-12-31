from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import TennisClubMemberRegistrationForm, TennisClubMemberLoginForm, \
    TennisClubMemberProfileForm
from .models import TennisClubMember


# Login view
def login_view(request):
    if request.method == 'POST':
        form = TennisClubMemberLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                user.last_login = now()  # Update last login timestamp
                user.save()
                login(request, user)
                return redirect('main')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = TennisClubMemberLoginForm()

    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Main view
@login_required
def main(request):
    return render(request, 'main.html')

# Members view
@login_required
def members(request):
    members = TennisClubMember.objects.all()  # Fetch all members
    return render(request, 'members/members.html', {'members': members})

# Member Registration view
def member_registration(request):
    if request.method == 'POST':
        form = TennisClubMemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form, including password hashing
            messages.success(request, "Registration successful!")
            return redirect('login')  # Redirect to a success page or login
        else:
            messages.error(request, "There were errors in the form. Please correct them.")
    else:
        form = TennisClubMemberRegistrationForm()

    return render(request, 'members/member_registration.html', {'form': form})

@login_required
def member_edit(request):
    user = request.user.tennisclubmember  # Assuming `TennisClubMember` is tied to `User`
    if request.method == 'POST':
        form = TennisClubMemberProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('member_edit')
    else:
        form = TennisClubMemberProfileForm(instance=user)

    return render(request, 'nenbers/member_edit.html', {'form': form})

# Courts view
@login_required
def courts(request):
    return render(request, 'courts.html')

# About view
@login_required
def about(request):
    return render(request, 'about.html')

# Contact view
@login_required
def contact(request):
    return render(request, 'contact.html')