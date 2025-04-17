# MultipleFiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password, ValidationError as PasswordValidationError
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserProfileUpdateForm
from .models import UserProfile

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    password_error = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, instance=user_profile)
        new_password = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # Password change logic
        if new_password or confirm_password:
            if new_password != confirm_password:
                password_error = "New password and confirm password do not match."
            else:
                try:
                    validate_password(new_password, user=request.user)
                except PasswordValidationError as e:
                    password_error = "; ".join(e.messages)
                else:
                    request.user.set_password(new_password)
                    # Don't save yet, wait for form validation

        if user_form.is_valid() and profile_form.is_valid() and not password_error:
            user_form.save()
            profile_form.save()
            if new_password and not password_error:
                request.user.save()
                update_session_auth_hash(request, request.user)  # Keep user logged in
                messages.success(request, 'Your profile and password have been updated successfully.')
            else:
                messages.success(request, 'Your profile has been updated.')
            # Refresh user object to get updated info
            request.user.refresh_from_db()
            return redirect('profile')
        else:
            if password_error:
                messages.error(request, f'Password error: {password_error}')
            else:
                messages.error(request, 'Please correct the errors in the form.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=user_profile)
    
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile,
        'user': request.user,
        'password_error': password_error,
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    from django.contrib.auth.models import User
    if request.method == 'POST':
        user_identifier = request.POST.get('user-identifier')
        password = request.POST.get('password')
        username = user_identifier
        # Check if user_identifier is an email
        if '@' in user_identifier:
            try:
                user_obj = User.objects.get(email=user_identifier)
                username = user_obj.username
            except User.DoesNotExist:
                username = None
        if username:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or any other page
        messages.error(request, 'Invalid username/email or password')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to login page


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been successfully deleted.')
        return redirect('home')
    return render(request, "accounts/delete_account.html")


def contact(request):
    return render(request, 'accounts/contact.html')  # accounts/templates/accounts/contact.html
