from django.db import models

class bday(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    msg = models.CharField(max_length=500)
    # song = models.CharField(upload_to ="bday/media") 