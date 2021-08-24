from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         # form = UserRegisterForm(request.POST,)
#         form = UserRegisterForm(request.POST, request.FILES)        
#         if form.is_valid():
#             instance = form.save(commit=False)
#             username = form.cleaned_data.get('username')
#             aadhar = form.cleaned_data.get('aadhar')
#             username.profile.aadhar = aadhar
#             form.save()
#             messages.success(request, f'Account created!Proceed to login')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request,'users/register.html',{'form':form})
def register(request):
    if request.method == "POST":
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(request, f'Registration complete! You may log in!')
            return redirect('login')
    else:
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})

# if not aadhar.isdigit() or not len(aadhar)==12:
#             raise forms.ValidationError("Invalid Aadhar ID")