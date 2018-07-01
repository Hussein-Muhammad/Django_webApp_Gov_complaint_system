from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .form import SignUpForm


# ------------------------------- handel Sign up page-----------------------#
def signup(request):
    if request.method == 'POST':  # Check for Post request
        form = SignUpForm(request.POST)  # Get SignUpForm and pass the request to form for validation
        context = {'form': form}  # context to be sent to html
        if form.is_valid():  # check the validation of Date
            code = request.POST['Code']  # Get Code from request
            user = form.save()  # Get user from form
            if code == '1234':  # Check the code
                user.is_superuser = True  # If code is true the admin is created If not a user is created
                user.save()  # Save new date
            auth_login(request, user)  # Mark this user as currently login
            return redirect('userHome')  # return to home page
    else:  # if no post request return to sign up page
        form = SignUpForm()
        context = {'form': form}
    return render(request, 'signup.html', context)
