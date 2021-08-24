from django.contrib import admin
from django.urls import path
from pages.views import home_view
from crime_report.views import crime_view, crime_report_staff_view, crime_report_detail, crime_report_user_view,cyber_report_detail 
from cyber_report_app.views import cyber_view, cyber_report_staff_view
from anonymous_app.views import anonymous_view,anonymous_report_staff_view,anonymous_report_detail
from dashboard.views import dashboard_view
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view , name='home'),
    path('crime_form/', crime_view, name='crime_form'),
    path('cyber_form/', cyber_view, name='cyber_form'),
    path('anonymous/', anonymous_view, name='anonymous_form'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('crime_staff/', crime_report_staff_view, name='staff_view'),
    path('cyber_staff/', cyber_report_staff_view, name='cyber_staff_view'),
    path('anonymous_staff/', anonymous_report_staff_view, name='anonymous_staff_view'),
    path('crime_detail/<int:my_id>/', crime_report_detail, name='crime_detail'),
    path('cyber_detail/<int:my_id>/', cyber_report_detail, name='cyber_detail'),
    path('anonymous_detail/<int:my_id>/', anonymous_report_detail , name='anonymous_detail'),
    path('user_view/', crime_report_user_view, name='user_view'),
    path('dashboard/', dashboard_view, name='dashboard'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                              
