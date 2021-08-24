from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
def file_size(value): # add this to some file where you can import it from
    limit = 100 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 100 MegaBytes.')
class Cyber_report(models.Model) :
    title = models.CharField(max_length=80, blank=False, unique=True)
    nature_of_crime = models.TextField(max_length=100,blank=False)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_date = models.DateField(blank=False)
    incident_time = models.TimeField(blank=False)
    evidence_img = models.ImageField( blank=True, null=True ,upload_to='images')
    evidence_vid = models.FileField(blank=True, null=True,validators=[file_size])
    status = models.CharField(max_length=21,default="Waiting",null=True, blank=True)
    
    def get_absolute_url(self):
        return f"/cyber_detail/{self.id}/" 
