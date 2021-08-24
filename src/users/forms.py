from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'first_name': forms.Textarea(
                                attrs={
                                    "placeholder" : 'First Name' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80', 
                                    'required': 'true'                                                                                                         
                               }
                            ),
            'last_name': forms.Textarea(
                                attrs={
                                    "placeholder" : 'Last Name' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80', 
                                    'required': 'true'                                                                                                         
                               }
                            ),
            'email': forms.Textarea(
                                attrs={
                                    "placeholder" : 'sample@company.com' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80', 
                                    'required': 'true'                                                                                                         
                               }
                            ),
            'aadhar': forms.Textarea(
                                attrs={
                                    "placeholder" : 'sample@company.com',
                                                                        
                                    "rows": '1',
                                    "type": 'integer',
                                    "maxlength" : '12', 
                                    'required': 'true'                                                                                                         
                               }
                            ),
        }
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['aadhar', 'phone']
# if not aadhar.isdigit() or not len(aadhar)==12:
#             raise forms.ValidationError("Invalid Aadhar ID")