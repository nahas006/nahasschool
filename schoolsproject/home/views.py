from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/detail')
        else:
            messages.info(request, "Invalid Entry")
            return redirect('login')
    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('register')
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('/home')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    return render(request, 'register.html')






def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, "You have been logged out")
    else:
        messages.info(request, "Your order is placed")

    # Set a session variable with the message
    request.session['custom_message'] = messages.info(request, "Your order is placed")

    return redirect('login/home')



def your_view(request):
    subject_links = {
        'computer_science': 'https://en.wikipedia.org/wiki/Computer_science',
        'commerce': 'https://en.wikipedia.org/wiki/Commerce',
        'Science': 'https://en.wikipedia.org/wiki/Science',
        'Arts': 'https://en.wikipedia.org/wiki/Arts',
        'Business': 'https://en.wikipedia.org/wiki/Business',
    }

    return render(request, 'home.html', {'subject_links': subject_links})
