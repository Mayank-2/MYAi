from django.urls import path,include
from Chat import views
urlpatterns = [
    path('Chat/',views.myAi,name='chat'),
    path('',views.home ,name='home'),
    path('main/',views.home2,name='main'),
    path('clear/',views.clearAsk,name="clear"),
    
    path('acc/',include('Account.urls')),

]