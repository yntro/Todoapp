from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import (UserRegisterForm, UserUpdateForm, TaskCreateUpdateForm,
                    UserUpdateAdminForm, ProfileUpdateAdminForm, TeamCreateUpdateForm,
                    TeamTasksCreateUpdateForm)
from .models import Task, Profile, Team



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context

class MyTasksView(LoginRequiredMixin, generic.ListView):
    template_name = "todoapp/my_tasks.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        return self.request.user.tasks.all().order_by("-date_created")

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateUpdateForm
    template_name = "todoapp/task_create.html"
    success_url = reverse_lazy("my_tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreateUpdateForm
    template_name = "todoapp/task_create.html"
    context_object_name = "task"
    success_url = reverse_lazy("my_tasks")

    def test_func(self):
        return self.request.user == self.get_object().user

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    template_name = "todoapp/task_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("my_tasks")

    def test_func(self):
        return self.request.user == self.get_object().user

class AdminView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = User
    template_name = "todoapp/admin.html"
    context_object_name = "users"

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.all()
        return context

class AdminUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateAdminForm
    template_name = "todoapp/admin_user.html"
    context_object_name = "user"
    success_url = reverse_lazy("admin")

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_form"] = ProfileUpdateAdminForm(instance=self.object.profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = UserUpdateAdminForm(request.POST, instance=self.object)
        profile_form = ProfileUpdateAdminForm(request.POST, instance=self.object.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return super().form_valid(user_form)

        context = self.get_context_data()
        context["form"] = user_form
        context["profile_form"] = profile_form

        return self.render_to_response(context)

class TeamCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Team
    form_class = TeamCreateUpdateForm
    success_url = reverse_lazy("admin")
    template_name = "todoapp/team_create.html"

    def test_func(self):
        return self.request.user.is_staff

class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Team
    form_class = TeamCreateUpdateForm
    template_name = "todoapp/team_create.html"
    context_object_name = "team"
    success_url = reverse_lazy("admin")

    def test_func(self):
        return self.request.user.is_staff

class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Team
    template_name = "todoapp/team_delete.html"
    context_object_name = "team"
    success_url = reverse_lazy("admin")

    def test_func(self):
        return self.request.user.is_staff

class TeamTasksView(LoginRequiredMixin, generic.ListView):
    template_name = "todoapp/team_tasks.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        team = self.request.user.profile.team

        return Task.objects.filter(user__profile__team=team).order_by("-date_created")

class TeamTasksCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Task
    form_class = TeamTasksCreateUpdateForm
    template_name = "todoapp/task_create.html"
    success_url = reverse_lazy("team_tasks")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["team"] = self.request.user.profile.team
        return kwargs

    def test_func(self):
        return self.request.user.profile.is_manager

class TeamTasksUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    form_class = TeamTasksCreateUpdateForm
    template_name = "todoapp/task_create.html"
    context_object_name = "task"
    success_url = reverse_lazy("team_tasks")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["team"] = self.request.user.profile.team
        return kwargs

    def test_func(self):
        return self.request.user.profile.is_manager and self.get_object().user.profile.team == self.request.user.profile.team

class TeamTasksDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    template_name = "todoapp/task_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("team_tasks")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["team"] = self.request.user.profile.team
        return kwargs

    def test_func(self):
        return self.request.user.profile.is_manager and self.get_object().user.profile.team == self.request.user.profile.team