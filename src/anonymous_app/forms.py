from django import forms
from .models import Anonymous_report
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

class AnonymousForm(forms.ModelForm):
    class Meta:
        model = Anonymous_report
        fields = [
                    'title',
                    'one_line_desc',
                    'description',
                    'incident_date',
                    'incident_time',
                    'evidence_img',
                    'evidence_vid',
                    'address_line', 
                    'address_city', 
                    'address_district', 
                    'address_state',    
                ]
        labels = {
            'title': 'Title',
            'incident_date': 'Aproximate Date of Crime',
            'incident_time': 'Aproximate Time of Crime',
            'address_line':'Address', 
            'address_city':'City', 
            'address_district':'District', 
            'address_state':'State',
        }
        widgets = {
             'title': forms.Textarea(
                                attrs={
                                    "placeholder" : 'Title' ,                                     
                                    "rows": '1',                                                                                                             
                               }
                             ),
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
             'one_line_desc': forms.Textarea(
                                attrs={
                                    "placeholder" : 'Short Description' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80',                                                                                                          
                               }
                            ),
             'address_line': forms.Textarea(
                                attrs={
                                    "placeholder" : 'Area of Crime' ,                                     
                                    "rows": '2',
                                    "type": 'text',
                                    "maxlength" : '255',                                                                                                          
                               }
                            ),
             'address_city': forms.Textarea(
                                attrs={
                                    "placeholder" : 'City' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80',                                                                                                          
                               }
                            ),
             'address_district': forms.Textarea(
                                attrs={
                                    "placeholder" : 'District' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80',                                                                                                          
                               }
                            ),
             'address_state': forms.Textarea(
                                attrs={
                                    "placeholder" : 'State',                                     
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