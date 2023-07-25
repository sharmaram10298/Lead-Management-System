from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    file = models.FileField(upload_to="files")

class Leads(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    address = models.CharField(max_length=1000)
    assigned_to = models.ForeignKey(User, related_name='assigned_leads', null=True, blank=True, on_delete=models.SET_NULL)
