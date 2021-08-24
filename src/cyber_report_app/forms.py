from django import forms
from .models import Cyber_report
from django.forms import ModelForm, FileField

from django.core.exceptions import ValidationError
# class CrimeForm(forms.Form):
#     title         = forms.CharField(
#                             label = 'Title',
#                             widget= forms.Textarea(
#                                 attrs={
#                                     "placeholder" : 'Title' ,
#                                     "maxlength" : '80',
#                                     "rows": '1',
#                                     "type": 'text',   
#                                 }
#                             )
#                         )
#     description   = forms.CharField(
#                             label = 'Description',
#                             widget= forms.Textarea(
#                                 attrs={
#                                     "placeholder" : 'Description' ,
#                                     "maxlength" : '80',
#                                     "rows": '5',
#                                     "type": 'text',   
#                                 }
#                             )
#                         )
#     one_line_desc = forms.CharField(
#                             label = 'One Line Description',
#                             widget= forms.Textarea(
#                                 attrs={
#                                     "placeholder" : 'Short Description' ,
#                                     "maxlength" : '80',
#                                     "rows": '1',
#                                     "type": 'text',   
#                                 }
#                             )
#                         )
#     incident_time = forms.DateField(
#                             label = 'Incident Date',
#                             widget= forms.SelectDateWidget(
#                                 empty_label=("Choose Year", "Choose Month", "Choose Day"),
#                                 attrs={
#                                     "placeholder" : 'Date' ,
#                                     "maxlength" : '80',
#                                     "rows": '1',
#                                     "type": 'date',
                                    
                                       
#                                 }
#                             )
#                         )
#     evidence_img = forms.ImageField(
#         label = 'Evidence Image',
#         required = False,
#     )
#     evidence_vid = forms.FileField(
#         label = 'Evidence Files',
#         required = False,
#     )

class CyberForm(forms.ModelForm):
    class Meta:
        model = Cyber_report
        fields = [
                    'title',
                    'nature_of_crime',
                    'description',
                    'incident_date',
                    'incident_time',
                    'evidence_img',
                    'evidence_vid',
                    'status',                       
                ]
        labels = {
             'incident_date': 'Date of Crime',
             'incident_time': 'Aproximate Time of Crime',
            'evidence_img': 'Evidence Image',
            'evidence_vid': 'Evidence Files',
        }
        widgets = {
            'status': forms.HiddenInput(),
             'incident_date': forms.SelectDateWidget(
                 
                                empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                attrs={
                                    "placeholder" : 'Date' ,
                                    "maxlength" : '80',
                                    "rows": '1',
                                    "type": 'date',
                                    
                                       
                               }
                            ),
              'incident_time': forms.Textarea(
                                attrs={
                                    "placeholder" : 'HOUR : MINUTE : SECONDS' ,                                     
                                    "rows": '1',
                                    
                                                                                                                                             
                               }
                             ),
             'nature_of_crime': forms.Textarea(
                                attrs={
                                    "placeholder" : 'Nature of Cyber Crime' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80',                                                                                                          
                               }
                            ),
             'description': forms.Textarea(
                                attrs={
                                    "placeholder" : 'Explain the Crime.',                                     
                                    "rows": '5',
                                    "type": 'text',
                                    "maxlength" : '80',                                                                                                          
                               }
                            ),
        }