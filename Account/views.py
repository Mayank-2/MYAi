from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Sign_up
from django.views import View
from django.contrib import messages
# Create your views here.

class CustomerRegistration(View):
    def get(self, request):
        form = Sign_up()
        return render(request, 'Account/signup.html', {'form': form})

    def post(self, request):
        form = Sign_up(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Signup Successfull! Please Login")
            return HttpResponseRedirect('/acc/accounts/login/')
        return render(request, 'Account/signup.html', {'form': form})
