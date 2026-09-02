from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from todoapp.models import Task, Profile, Team


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ["username",'first_name', 'last_name', "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class TaskCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", 'status']

class UserUpdateAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "username"]

class ProfileUpdateAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['team', 'is_manager']

class TeamCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'manager']

class TeamTasksCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'user']

    def __init__(self, *args, team=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["user"].queryset = User.objects.filter(
            profile__team=team
        )