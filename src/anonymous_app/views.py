from django.shortcuts import render, redirect
from .forms import AnonymousForm
from .models import Anonymous_report

# Create your views here.
def anonymous_report_staff_view(request):
    queryset = Anonymous_report.objects.all()
    context = {
        "object_anonymous_list": queryset
    }
    return render(request,"staff_anonymous.html",context)
def anonymous_report_detail(request, my_id):
    obj3 = Anonymous_report.objects.get(id=my_id)
    context = {
        'object': obj3 ,      
    }
    return render(request,"anonymous_detail.html", context)
def anonymous_view(request):
    my_form = AnonymousForm()
    if request.method == "POST":
        my_form = AnonymousForm(request.POST, request.FILES)
        if my_form.is_valid():
            my_form.save()
            # Crime_report.objects.create(**my_form.cleaned_data)
            return redirect('anonymous_form')   
            
    context = {
        "form": my_form
    }
    return render(request,"anonymous_form.html", context)
