from django.shortcuts import render, redirect
from .forms import CyberForm
from .models import Cyber_report
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


@login_required
def cyber_view(request):
    my_form = CyberForm()
    if request.method == "POST":
        my_form = CyberForm(request.POST, request.FILES)
        if my_form.is_valid():
            instance = my_form.save(commit=False)
            instance.user = request.user
            instance.save()
            # Crime_report.objects.create(**my_form.cleaned_data)
            return redirect('cyber_form')   
            
    context = {
        "form": my_form
    }
    return render(request,"cyber_form.html", context)
# def cyber_report_user_view(request):
#     queryset = Cyber_report.objects.filter(user=User.objects.get (username=request.user ))
#     context = {
#         "object_cyber_list": queryset
#     }
#     return render(request,"user_view.html",context)
def crime_report_detail(request, my_id):
    obj = Cyber_report.objects.get(id=my_id)
    my_form = CyberForm(request.POST, request.FILES)
    my_status = request.POST.get("status")
    Cyber_report.objects.filter(id=my_id).update(status=my_status)
    context = {
        'object': obj
    }
    return render(request,"crime_detail.html", context)



@staff_member_required
def cyber_report_staff_view(request):
    queryset = Cyber_report.objects.all()
    context = {
        "object_cyber_list": queryset
    }
    return render(request,"staff_cyber.html",context)


