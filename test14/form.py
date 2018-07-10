from django import forms
from .models import Complaint
from .models import Details


# --------------------------------new complaint form---------------------------------------#
# part1
class NewComplaintForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(),
                                  max_length=100)  # make field for description and limit it to 100 char
    priority = forms.IntegerField(max_value=10, min_value=1, show_hidden_initial=1,
                                  help_text='(1-10)')  # make field for priority and limit it to 10 max value and 1 min vlaue

    class Meta:  # organize form fields
        model = Complaint
        fields = ['name', 'description', 'priority']


# part2
class NewComplaintDForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Detailed Complaint goes here'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )  # make field for massage and limit it to 4000 char and set help text

    class Meta:  # organize form fields
        model = Details
        fields = ['message']


# ----------------------------------Reply form--------------------------------------------------#
class ReplayForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Reply goes here'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )  # make field for massage and limit it to 4000 char and set help text

    class Meta:  # organize form fields
        model = Details
        fields = ['message']
