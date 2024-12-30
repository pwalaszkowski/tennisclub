from django.shortcuts import render, redirect
from .forms import TennisClubMemberRegistrationForm

# Login view
def login(request):
    return render(request, 'login/login.html')

# Main view
def main(request):
    return render(request, 'main.html')

# Members view
def members(request):
    return render(request, 'members.html')

# Member Registration view
def member_registration(request):
    if request.method == 'POST':
        form = TennisClubMemberRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form which includes password hashing
            return redirect('login')  # Redirect to a success page or login
    else:
        form = TennisClubMemberRegistrationForm()

    return render(request, 'registration/member_registration.html', {'form': form})

# Courts view
def courts(request):
    return render(request, 'courts.html')

# About view
def about(request):
    return render(request, 'about.html')

# Contact view
def contact(request):
    return render(request, 'contact.html')