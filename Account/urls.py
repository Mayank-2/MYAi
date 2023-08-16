from django.urls import path,include
from Account import views
from django.contrib.auth import views as auth_views
from Account.forms import Log_in 
from django.conf.urls.static import static  
from django.conf import settings
# from Account.views import add_to_cart_,cart

urlpatterns = [

    path('signup/',views.CustomerRegistration.as_view(),name='signup'),

    path('accounts/login/',auth_views.LoginView.as_view(template_name = 'Account/login.html', authentication_form =Log_in),name='login'),

    path('logout/',auth_views.LogoutView.as_view(),name='logout'), 
]