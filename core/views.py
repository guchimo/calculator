from django.shortcuts import render,redirect
from .models import History
from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    )
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'core/base.html'
    

def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('calculate_view')
        else:
            messages.error(request, "Incorrect credentials try again ")

    return render(request, 'core/user_login.html', {'form': form})


def user_registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            return redirect('login_view')

    return render(request, 'core/user_registration.html', {'form': form})


@login_required
def calculate(request):
    if request.method == "POST":
        expression = request.POST.get('expression')
        try:
            output = eval(expression)
            History.objects.create(input_expression=expression, output_result=output, owner=request.user)
        except SyntaxError:
            output = "Invalid expression please try again"
        except ZeroDivisionError:
            output = "Infinite"
        return render(request, 'core/calculator.html', {'result': output, 'expression': expression})

    return render(request, 'core/calculator.html')


class HistoryListView(LoginRequiredMixin, ListView):
    model = History

    def get_queryset(self):
        return History.objects.filter(owner=self.request.user)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = User
    success_url = '/'
    template_name = 'core/user_update_form.html'







