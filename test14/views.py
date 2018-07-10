from django.shortcuts import render, redirect
from test14.models import Complaint, Details
from .form import NewComplaintDForm, NewComplaintForm, ReplayForm


# ------------------------------------Functions that handel Detail.html page---------------------------------#
def details(request, pk):
    item = Complaint.objects.get(pk=pk)  # Get all the complaint in the DataBase with id(pk)
    messages = Details.objects.filter(complaint_id=pk)  # Filter the massage related to the complaint above
    user = request.user  # Get the currently login user
    if not user.is_superuser:  # Check if the user is admin {to mark the complaint answer by the admin}
        item.isRead = True  # Mark not read
        item.save()  # Add(save) the new data to the complaint
    if request.method == 'POST' and 'Post' in request.POST:  # Check if there is any request to Post new massage
        form = ReplayForm(request.POST)  # Pass the request to the form to validate it
        context = {'item': item, 'details': messages, 'form': form}  # Context to be send to the html page
        if form.is_valid():  # Check the validation of the data sent by the user
            mes = request.POST['message']  # Get massage from the request
            messages.create(complaint_id=pk, message=mes,
                            created_by=user)  # Create massage with the content in the form sent by the user
            if user.is_superuser:  # Check if the user is admin {to mark the complaint answer by the admin}
                item.isRead = False  # Mark as not read
                item.isInProgress = True  # Mark inProgress
                item.save()  # Add(save) the new data to the complaint
            else:
                item.isRead = True  # Mark as read
                item.save()  # Add(save) the new data to the complaint
            return redirect("userHome")  # return to the Home page
        else:
            return render(request, 'Details.html', context)  # If the Data sent wasn't valid Load Details.html
    elif request.method == 'POST' and 'Solved' in request.POST:  # Check if there is any request to Mark complaint as solved
        item.isSolved = True  # Mark as Solved complaint
        item.isRead = False  # Mark as Read
        item.isInProgress = False  # Mark as not in progress
        item.save()  # Save new data
        return redirect("userHome")  # return to home page
    else:  # If there are no request to post Load the page
        form = ReplayForm()  # Get reply form with no request pass to prevent not valid error
        context = {'item': item, 'details': messages, 'form': form}  # Context to be send to the html page
        return render(request, 'Details.html', context)  # Return to Details.html


# ------------------------------------Functions that handel NewComplaint.html page---------------------------------#
def new_complaint(request):
    complaints = Complaint.objects.all()  # Get all the complaints
    if request.method == 'POST':  # Check if there is any request to post new complaint
        form = NewComplaintForm(request.POST)  # Pass the request to the form to validate it
        form1 = NewComplaintDForm(request.POST)  # Pass the request to the form1 to validate it
        users = request.user  # Get the currently login user
        context = {'item': complaints, 'form': form, 'form1': form1}  # Context to be send to the html page
        if form1.is_valid() and form.is_valid():  # Check the validation of the data sent by the user
            name = request.POST['name']  # Get name from the request
            des = request.POST['description']  # Get description from the request
            mes = request.POST['message']  # Get massage from the request
            per = request.POST['priority']  # Get priority from the request
            complaints.create(name=name, des=des, isSolved=False, isRead=True, per=per,
                              starter=users)  # Create complaint with the content in the form sent by the user
            complaint = complaints.last()  # Get the last added complaints
            messages = Details.objects.create(complaint=Complaint.objects.get(id=complaint.id), message=mes,
                                              created_by=users)  # Create massage with the content in the form sent by the user
            return redirect("userHome")  # redirect to user home page
        else:
            return render(request, 'NewComplaint.html', context)  # return to NewComplaint.html
    else:
        if request.user.is_superuser:  # Check if user is an admin
            return redirect("adminHome")  # if the user is an admin redirect to admin home page
        form1 = NewComplaintDForm()  # Get reply form with no request pass to prevent not valid error
        form = NewComplaintForm()  # Get reply form with no request pass to prevent not valid error
        context = {'item': complaints, 'form': form, 'form1': form1}
        return render(request, 'NewComplaint.html', context)


# ------------------------------------Functions that handel Home.html page---------------------------------#
# Handel request to home page from both users and admins #
def home(request):
    user = request.user  # Get the login user
    if not user.is_superuser:  # Check if he is an admin
        complaints = Complaint.objects.filter(
            starter=user)  # Filter the complaint with starter is the logen user sorted already from late to newer
        Compliant_list_Alpha = sorted(complaints, key=lambda x: x.name.lower())  # sort complaint according to alphabet
        complaint_list_date = complaints[::-1]  # reverse it to show newer first
        Compliant_list_Priority = sorted(complaints, key=lambda x: x.per,
                                         reverse=True)  # reversed so higher priority first
        context = {'Compliant_list_date': complaint_list_date, 'Compliant_list_Priority': Compliant_list_Priority,
                   'Compliant_list_Alpha': Compliant_list_Alpha,
                   'user': user}  # Context to be send to the html page
        return render(request, 'Home.html', context)  # return to home.html
    else:
        return redirect('adminHome')  # if the user is admin redirect to admin home page


# Handel request to home page from admins #
def admin_home(request):
    user = request.user  # Get the login user
    if not user.is_superuser:  # Check if he is an admin
        return redirect("userHome")  # if the user is not an admin redirect to user home page
    complaints = Complaint.objects.filter(
        isSolved=False)  # Filter the not solved complaint sorted, already from late to newer
    Compliant_list_Alpha = sorted(complaints, key=lambda x: x.name.lower())  # sort complaint according to alphabet
    complaint_list_date = complaints[::-1]  # reverse it to show newer first
    Compliant_list_Priority = sorted(complaints, key=lambda x: x.per, reverse=True)  # reversed so higher priority first
    context = {'Compliant_list_date': complaint_list_date, 'Compliant_list_Priority': Compliant_list_Priority,
               'Compliant_list_Alpha': Compliant_list_Alpha,
               'user': user}  # Context to be send to the html page
    return render(request, 'Home.html', context)  # return to home.html


# Handel request to home page from admins when he want to see solved complaints #
def solved(request):
    user = request.user  # Get the login user
    if not user.is_superuser:  # Check if he is an admin
        return redirect("userHome")  # if the user is not an admin redirect to user home page
    complaints = Complaint.objects.filter(
        isSolved=True)  # Filter the solved complaint sorted, already from late to newer
    Compliant_list_Alpha = sorted(complaints, key=lambda x: x.name.lower())  # sort complaint according to alphabet
    complaint_list_date = complaints[::-1]  # reverse it to show newer first
    Compliant_list_Priority = sorted(complaints, key=lambda x: x.per, reverse=True)  # reversed so higher priority first
    context = {'Compliant_list_date': complaint_list_date, 'Compliant_list_Priority': Compliant_list_Priority,
               'Compliant_list_Alpha': Compliant_list_Alpha,
               'user': user}  # Context to be send to the html page
    return render(request, 'Home.html', context)  # return to home.html


# Handel request to home page from users when they want to see not read complaints#
def not_read(request):
    user = request.user  # Get the login user
    if user.is_superuser:  # Check if he is an admin
        return redirect("adminHome")  # if the user is an admin redirect to admin home page
    complaints = Complaint.objects.filter(
        isRead=False, starter=user)  # Filter the not raed complaint sorted already from late to newer
    Compliant_list_Alpha = sorted(complaints, key=lambda x: x.name.lower())
    complaint_list_date = complaints[::-1]  # reverse it to show newer first
    Compliant_list_Priority = sorted(complaints, key=lambda x: x.per, reverse=True)  # reversed so higher priority first
    context = {'Compliant_list_date': complaint_list_date, 'Compliant_list_Priority': Compliant_list_Priority,
               'Compliant_list_Alpha': Compliant_list_Alpha,
               'user': user}  # Context to be send to the html page
    return render(request, 'Home.html', context)  # return to home.html


#   Handel request to home page from users when they want to see in progress complaints#
def in_progress(request):
    user = request.user  # Get the login user
    complaints = Complaint.objects.filter(
        isInProgress=True, starter=user)  # Filter the not raed complaint sorted already from late to newer
    Compliant_list_Alpha = sorted(complaints, key=lambda x: x.name.lower())
    complaint_list_date = complaints[::-1]  # reverse it to show newer first
    Compliant_list_Priority = sorted(complaints, key=lambda x: x.per, reverse=True)  # reversed so higher priority first
    context = {'Compliant_list_date': complaint_list_date, 'Compliant_list_Priority': Compliant_list_Priority,
               'Compliant_list_Alpha': Compliant_list_Alpha,
               'user': user}  # Context to be send to the html page
    return render(request, 'Home.html', context)  # return to home.html
