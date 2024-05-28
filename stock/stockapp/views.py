from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy

from stock.stockapp.migrations.form import CreateUserForm


def index(request):
    return HttpResponse("Hello, world.")


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration/Signup.html', context)

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/Login.html'

    def get_success_url(self):
        return reverse_lazy('stock:index')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('stock:index')

