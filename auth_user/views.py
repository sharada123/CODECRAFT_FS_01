from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import CustomUser
from django.contrib.auth import authenticate, login,logout
# Create your views here.

# Home Page
def homepage(request):
    form = RegistrationForm()
    return render(request, 'home.html', {'form': form})

# Register Page
def register_page(request):
    return render(request, 'register.html', {'form': RegistrationForm()})

# Login Page
def login_page(request):
    return render(request, 'login.html', {'form': LoginForm()})

@login_required(login_url='Login') 
def admin_page(request):
    return render(request, 'admin.html')


@login_required(login_url='Login')
def user_page(request):
    return render(request, 'user.html')
# User Registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if user already exists BEFORE saving
            if CustomUser.objects.filter(Q(username=username) | Q(email=email)).exists():
                return render(request, 'register.html', {'form': form, 'error': 'Username or Email already exists!'})

            # Check if passwords match
            if password != confirm_password:
                return render(request, 'register.html', {'form': form, 'error': 'Password and Confirm Password did not match!'})

            # Save the user
            user = form.save(commit=False)
            user.set_password(password)  # Hash the password
            user.save()

            return redirect('LoginPage')  # Redirect to login after successful registration
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'form': RegistrationForm()})


# User Login


def login_user(request):
    print('Login view function called')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("Form valid:", form.is_valid())
        print("Form data:", form.data)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = request.POST.get('password')  # Use raw password

            user = authenticate(request, username=username, password=password)
            print("Authenticated User:", user)

            if user:
                login(request, user)  # Log the user in
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                elif user.role == 'user':
                    return redirect('user_dashboard')
                else:
                    return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password!'})

        else:
            print("Form errors:", form.errors)  # Debugging

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})  # Show login form again



# User Logout
def logout_user(request):
    logout(request)
    return redirect('LoginPage')  # Redirect to login page after logout
