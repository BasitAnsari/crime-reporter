from django.shortcuts import render
from crime_report.models import Crime_report
from anonymous_app.models import Anonymous_report
from cyber_report_app.models import Cyber_report
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from datetime import date, timedelta, datetime
from .forms import DateForm
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import json
from bokeh.io import curdoc
from bokeh.models import DatetimeTickFormatter, HoverTool
from bokeh.themes import built_in_themes
# Create your views here.
def dashboard_view(request):
    date_set = []
    count_set = []
    if request.method ==  'POST':
        date_from= request.POST.get('date_from')
        date_to= request.POST.get('date_to')
        start_date = datetime.strptime(date_from, '%Y-%m-%d')
        end_date = datetime.strptime(date_to, '%Y-%m-%d')
        delta = timedelta(days=1)
        while start_date <= end_date:
            date_set.append(start_date)
            c_set = Crime_report.objects.filter(timestamp__date__lte=start_date,timestamp__date__gte=start_date)
            count = len(c_set)
            count_set.append(count)
            start_date += delta
    x= date_set
    y= count_set
    curdoc().theme = 'dark_minimal'
    plot = figure( plot_height=300,
           title="Reports Per Day",
           x_axis_type='datetime',
                tools='hover')
    plot.line(x,y,line_width=2)
    hover = plot.select(dict(type=HoverTool))
    hover.tooltips = [
            ('(Reports)', '(@y)')
            ]
    plot.xaxis[0].formatter = DatetimeTickFormatter(days="%Y/%m/%d")
    plot.xaxis.ticker.desired_num_ticks = 6
    script, div = components(plot)
    context = {
        'script':script,
        'div': div
    }
    return render(request,"dashboard/dashboard.html",context)