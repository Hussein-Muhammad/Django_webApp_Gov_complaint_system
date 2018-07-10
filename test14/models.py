from django.db import models
# -------------------------------------------User model-----------------------------------------#
# We used the user model in the python by implement User from Auth lib
from django.contrib.auth.models import User


# -------------------------------------------Complaint model------------------------------------#
class Complaint(models.Model):
    name = models.CharField(max_length=30)  # The title of the complaint
    des = models.CharField(max_length=100)  # Short description
    isSolved = models.BooleanField()  # boolean to know if the admin Solve the Complaint
    postDate = models.DateField(auto_now_add=True)  # hold Date of creation
    starter = models.ForeignKey(User, null=True, related_name="complaints",
                                on_delete=models.DO_NOTHING)  # hold the user created the complaint (Link to user model)
    isRead = models.BooleanField()  # boolean to know if the user read the massage
    per = models.IntegerField()  # hold priority of complain (user determine it)
    isInProgress = models.BooleanField(default=False)  # boolean to know if the adin working on complaint

    def __str__(self):  # To string function
        return self.name  # Return name


# -------------------------------------------Details model-----------------------------------------#
class Details(models.Model):
    complaint = models.ForeignKey(Complaint, related_name="post",
                                  on_delete=models.DO_NOTHING)  # hold complaint id related to massage (link to complaint)
    message = models.TextField(max_length=4000)  # hold massage
    created_at = models.DateTimeField(auto_now_add=True)  # hold Date of creation of massage
    created_by = models.ForeignKey(User, null=True, related_name="+",
                                   on_delete=models.DO_NOTHING)  # hold the user created the complaint (Link to user model)
