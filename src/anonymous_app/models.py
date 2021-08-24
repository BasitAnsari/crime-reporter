from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def file_size(value): # add this to some file where you can import it from
    limit = 100 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 100 MegaBytes.')
class Anonymous_report(models.Model) :
    title = models.CharField(max_length=80, blank=False, unique=True)
    one_line_desc = models.TextField(max_length=100,blank=False)
    description = models.TextField(max_length=500)
    # userid = models.ForeignKey(User,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_date = models.DateField(blank=False)
    incident_time = models.TimeField(blank=False)
    evidence_img = models.ImageField( blank=True, null=True ,upload_to='images')
    evidence_vid = models.FileField(blank=True, null=True,validators=[file_size]) 
    address_line = models.TextField(max_length=255,blank=False)
    address_city = models.TextField(max_length=100,blank=False)
    address_district = models.TextField(max_length=100,blank=False)
    address_state = models.TextField(max_length=100,blank=False)
    def get_absolute_url(self):
            return f"/anonymous_detail/{self.id}/" 
