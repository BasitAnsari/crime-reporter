from django.shortcuts import render, redirect
from .forms import CrimeForm, SearchForm
from .models import Crime_report
from anonymous_app.models import Anonymous_report
from cyber_report_app.models import Cyber_report
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
import json

# Create your views here.
@login_required
def crime_view(request):
    my_form = CrimeForm()
    if request.method == "POST":
        my_form = CrimeForm(request.POST, request.FILES)
        if my_form.is_valid():
            instance = my_form.save(commit=False)
            instance.user = request.user
            instance.save()
            # Crime_report.objects.create(**my_form.cleaned_data)
            return redirect('crime_form')           
    context = {
        "form": my_form
    }
    return render(request,"crime_form.html", context)

@login_required
def crime_report_user_view(request):
    queryset = Crime_report.objects.filter(user=User.objects.get (username=request.user ))
    queryset2 = Cyber_report.objects.filter(user=User.objects.get (username=request.user ))
    queryset_count = queryset.count()
    queryset_count2 = queryset2.count()
    context = {
        "object_list": queryset ,
        "object_cyber_list": queryset2,
        "queryset_count": queryset_count,
        "queryset_count2": queryset_count2,
         
    }
    return render(request,"user_view.html",context)
def crime_report_detail(request, my_id):
    obj = Crime_report.objects.get(id=my_id)
    
    context = {
        'object': obj,   
    }
    return render(request,"crime_detail.html", context)
def cyber_report_detail(request, my_id):
    obj2 = Cyber_report.objects.get(id=my_id)
    context = {
        'object': obj2 ,      
    }
    return render(request,"cyber_detail.html", context)


@staff_member_required
def crime_report_staff_view(request):
    queryset = Crime_report.objects.all()
    form = SearchForm(request.POST or None)
    if request.method == 'POST':
        date_from= request.POST.get('date_from')
        date_to= request.POST.get('date_to')
        queryset = Crime_report.objects.filter(timestamp__date__lte=date_to,timestamp__date__gte=date_from)
        date_set = []
        count_set = []
        # print(Crime_report.objects.get(id=5).timestamp.date())
        from datetime import date, timedelta, datetime

        start_date = datetime.strptime(date_from, '%Y-%m-%d')
        end_date = datetime.strptime(date_to, '%Y-%m-%d')
        delta = timedelta(days=1)
        while start_date <= end_date:
            print (start_date.strftime("%Y-%m-%d"))
            date_set.append(start_date.strftime("%Y-%m-%d"))
            c_set = Crime_report.objects.filter(timestamp__date__lte=start_date,timestamp__date__gte=start_date)
            count = len(c_set)
            count_set.append(count)
            start_date += delta
            print(count_set)  
        date_list = json.dumps(date_set)
        count_list = json.dumps(count_set)
    context = {
        "form": form,
        "object_list": queryset
    }
    return render(request,"staff_view.html",context)
def crime_report_detail(request, my_id):
    obj = Crime_report.objects.get(id=my_id)
    my_form = CrimeForm(request.POST, request.FILES)
    my_status = request.POST.get("status")
    Crime_report.objects.filter(id=my_id).update(status=my_status)
    context = {
        'object': obj
    }
    return render(request,"crime_detail.html", context)

