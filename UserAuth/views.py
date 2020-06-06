from django.shortcuts import render, redirect

# Auth Forms (Login.Logout,Signin,Signout)
from django.contrib.auth.forms import UserCreationForm
# Customized Auth Forms As Needed


# Messages For Inforamtion
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account has been created for {username}!')

           # return redirect()

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
