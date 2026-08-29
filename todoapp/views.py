from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserUpdateForm, TaskCreateForm
from .models import Task


class HomeView(generic.TemplateView):
    template_name = 'todoapp/home.html'

class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = "todoapp/signup.html"
    success_url = reverse_lazy("login")

class ProfileView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "todoapp/profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

class MyTasksView(LoginRequiredMixin, generic.ListView):
    template_name = "todoapp/my_tasks.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        return self.request.user.tasks.all()

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "todoapp/task_create.html"
    success_url = reverse_lazy("my_tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
