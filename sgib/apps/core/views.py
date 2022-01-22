from sgib.apps.core.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required(login_url="login/")
def index(request):
    return render(request, 'index.html')


def do_login(request):
    context = dict()
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is not None:
                login(request, user)

                return redirect('index')

            form.add_error(None, "Credenciais incorretas")

        context['form'] = form

    return render(request, 'login.html', context)
