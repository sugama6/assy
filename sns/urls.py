from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assy.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', TemplateView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('accounts/logout/', TemplateView.as_view(template_name = 'logout.html'), name='logout'),
    path('accounts/signup/', TemplateView.as_view(template_name = 'signup.html'), name='signup'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(template_name='account/password/reset.html'), name='reset'),
    path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(template_name='account/password/reset_done.html'), name="reset_done"),
    path('accounts/password_reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="account/password/reset_confirm.html"), name="reset_confifm"),
    #path('accounts/reset/done/', .as_view(template_name='account/password_change_done.html'), name="password_change_done")
]