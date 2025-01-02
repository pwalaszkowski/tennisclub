from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import TennisClubMemberRegistrationForm, TennisClubMemberLoginForm, \
    TennisClubMemberProfileForm, CourtForm, ReservationForm
from .models import TennisClubMember, Court, Reservation


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
            # Extract cleaned data
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            try:
                # Create the User object
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                )

                # Create the TennisClubMember object
                TennisClubMember.objects.create(
                    user=user,
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    phone_number=data.get('phone_number'),
                    date_of_birth=data.get('date_of_birth'),
                    address=data.get('address'),
                    membership_type=data.get('membership_type'),
                )

                messages.success(request, "Registration successful!")
                return redirect('login')  # Redirect to login or success page
            except Exception as e:
                messages.error(request, f"An error occurred during registration: {e}")
                return redirect('member_registration')
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

    return render(request, 'members/member_edit.html', {'form': form})

# Courts view
@login_required
@login_required
def courts(request):
    courts_list = Court.objects.all()  # Fetch all courts
    reservations = Reservation.objects.all() # Fetch all reservations

    return render(request, 'courts/courts.html', {'courts': courts_list, 'reservations': reservations})

@login_required
def court_add(request):
    if request.method == 'POST':
        form = CourtForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Court added successfully!")
            return redirect('courts')  # Redirect to court list after adding
        else:
            messages.error(request, "Failed to add court. Please check the form.")
    else:
        form = CourtForm()
    return render(request, 'courts/court_add.html', {'form': form})

@login_required
def court_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.member = request.user.tennisclubmember  # Link to logged-in member
            reservation.save()
            messages.success(request, "Reservation successful!")
            return redirect('courts')
        else:
            messages.error(request, "Failed to make reservation. Please check the form.")
    else:
        form = ReservationForm()
    return render(request, 'courts/court_reservation.html', {'form': form})


# About view
@login_required
def about(request):
    return render(request, 'about.html')

# Contact view
@login_required
def contact(request):
    return render(request, 'contact.html')