from django import forms
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls.conf import path
from django.views.generic import ListView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, MentorForm, SubjectsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import StudentCreateForm, MentorCreateForm, GroupCreateForm
# Create your views here.







@login_required(login_url="sign_up")
def dashboard(request):
    subject = Subjects.objects.all()
    students = (len(Subjects.objects.filter(students__gte=1)) * 100) / 100
    # print(students)
    context = {
        'subjects': subject,
        'studen': str(int(students)) 
    }
    return render(request, 'mainapp/dashboard.html', context)


@login_required(login_url="sign_up")
def tables(request):
    mentors = Mentor.objects.all()
    students = Student.objects.all()
    group = Group.objects.all()
    payment = Student.objects.all()
    context = {
        "mentors": mentors,
        "students": students,
        "payment": payment,
        'groups': group
    }
    return render(request, 'mainapp/student_tables.html', context)


def create_student(request):
    form = StudentCreateForm()
    if request.method == "POST":
        form = StudentCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tables")
    else:
        form = StudentCreateForm()

    context = {
        "form": form,
    }
    return render(request, "mainapp/create_student.html", context)


def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form  = StudentCreateForm(instance=student)
    if request.method == "POST":
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            return redirect('tables')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_student.html", context)


def delete_student(request, pk):
    student =Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('tables')

    context = {
        "student": student
    }

    return render(request, 'mainapp/delete_student.html', context)



def create_mentor(request):
    form = MentorCreateForm()
    if request.method == "POST":
        form = MentorCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tables")
    else:
        form = MentorCreateForm()

    context = {
        "form": form,
    }
    return render(request, "mainapp/create_mentor.html", context)


def update_mentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    form  = MentorCreateForm(instance=mentor)
    if request.method == "POST":
        form = MentorCreateForm(request.POST, instance=mentor)
        if form.is_valid:
            form.save()
            return redirect('tables')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_mentor.html", context)



def delete_mentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    if request.method == 'POST':
        mentor.delete()
        return redirect('tables')

    context = {
        "mentor": mentor
    }

    return render(request, 'mainapp/delete_mentor.html', context)



def create_group(request):
    form = GroupCreateForm()
    if request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tables")
    else:
        form = GroupCreateForm()

    context = {
        "form": form,
    }
    return render(request, "mainapp/create_group.html", context)



def update_group(request, pk):
    group = Group.objects.get(id=pk)
    form  = GroupCreateForm(instance=group)
    if request.method == "POST":
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid:
            form.save()
            return redirect('tables')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_group.html", context)



def delete_group(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('tables')

    context = {
        "group": group
    }

    return render(request, 'mainapp/delete_group.html', context)


@login_required(login_url="sign_up")
def billing(request):
    return render(request, 'mainapp/billing.html')


@login_required(login_url="sign_up")
def profile(request):
    return render(request, 'mainapp/profile.html')


@login_required(login_url="sign_up")
def rtl(request):
    return render(request, 'mainapp/rtl.html')


def sign_in(request):
    return render(request, 'mainapp/sign_in.html')


def sign_up(request):
    return render(request, 'mainapp/sign_up.html')


@login_required(login_url="sign_up")
def virtual_reality(request):
    return render(request, 'mainapp/virtual_reality.html')
    

def register_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            # print(form)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('sign_in')
            else:
                # print('sadasdasdsadasdasdasd')
                return redirect('sign_in')
        context = {
            'form': form
            }
        return render(request, 'mainapp/sign_up.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            # else:
            #     messages.info(request, "ERORR")
            
        context = {}

        return render(request, 'mainapp/sign_in.html', context)


def logout_user(request):
    logout(request)
    return redirect('sign_up')


def subjects(request):
    form = SubjectsForm
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('')
        else:
            return redirect('')
    else:
        return redirect('')


class MentorUpdateView(UpdateView):
    model = Mentor
    # form_class = MentorForm
    template_name = 'mainapp/update.html'
    template_name_suffix = '_update_form'
    fields = ['phone', 'email', 'full_name']
    success_url = 'dashboard'


class NewsDeleteView(DeleteView):
    template_name = 'news/details_view.html'
    context_object_name = 'article'


# def edit(request, pk):
#     if request.method == 'POST':
#         mentor = Mentor.objects.get(id=pk)
#         mentor.full_name = request.POST.get('name')
#         mentor.email = request.POST.get('eamil')
#         mentor.phone = request.POST.get('phone')
#         mentor.save()
#     else:
#         return redirect('dashboard')


def group_filter(request, pk):
    mentors = Mentor.objects.all()
    if pk != None:
        students = Student.objects.filter(group=pk)
    else:
        students = Student.objects.all()
    context = {
        'students': students,
        'mentors': mentors
    }
    return render(request, 'mainapp/tables.html', context)


def payment_status_filter(request, pk):
    mentors = Mentor.objects.all()
    if pk != None:
        print(pk)
        students = Student.objects.filter(Q(payment_status=pk) | Q(gender=pk))
    else:
        students = Student.objects.all()
    context = {
        'students': students,
        'mentors': mentors
    }
    return render(request, 'mainapp/tables.html', context)





# def gender_filter(request, pk):
#     mentors = Mentor.objects.all()
#     students = Student.objects.all()
#     print(pk)
#     if pk != None :
#         students = Student.objects.filter(gender=pk)
#         print('POOOOST')
#     else:
#         students = Student.objects.all()
#     context = {
#         'students': students,
#         'mentors': mentors
#     }
#     return render(request, 'mainapp/tables.html', context)


# class GroupView(ListView):
#     model = Group
#     queryset = Group.objects.filter()
#     template_name = 'mainapp/tabels.html'
