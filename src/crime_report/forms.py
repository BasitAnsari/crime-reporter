from django import forms
from .models import Crime_report
from django.forms import ModelForm, FileField
from django.core.exceptions import ValidationError

class SearchForm(forms.Form):
    date_from = forms.DateField(widget= forms.DateInput(attrs={'type':'date'}))
    date_to = forms.DateField(widget= forms.DateInput(attrs={'type':'date'}))

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime_report
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
                    'status',
                    
                       
                ]
        labels = {
            'one_line_desc': 'One Line description',
            'incident_date': 'Date of Crime',
            'incident_time': 'Aproximate Time of Crime',
            'address_line':'Address', 
            'address_city':'City', 
            'address_district':'District', 
            'address_state':'State',
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
        

        
        
 
        

        