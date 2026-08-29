from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

class HomeView(generic.TemplateView):
    template_name = 'todoapp/home.html'

class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = "todoapp/signup.html"
    success_url = reverse_lazy("login")
