from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Forms
from .forms import LoginForm

# Authentication Modules
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

# Flash Message
from django.contrib import messages

# Create your views here.
def user_login(request):
    # date = datetime.now()
    # Year,WeekNum,DOW = date.isocalendar() 
    # print(WeekNum)
    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Return a message after authentication
            messages.success(request, f'You have successfully logged-in to your account.')
            return redirect('account:index')
        else:
            messages.warning(request, f'There seems to be a problem with your account. Please contact your administrator for assistance.')

            return redirect('account:index')

    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)