from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.db.models import fields
from .models import * 
from django.forms import fields


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['phone', 'full_name', 'email']


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["full_name", "birth_date", "phone", "email", "group", "payment_status", "gender"]


class MentorCreateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ["full_name", "birth_date", "phone", "email", "spesification", "developer_tech", "level"]


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "spesification", "developer_tech", "mentor", "start_date", "finish_date"]