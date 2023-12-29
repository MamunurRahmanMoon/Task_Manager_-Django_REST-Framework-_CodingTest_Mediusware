from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import SignupForm, TaskForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('task_list') 

class CustomLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('login')


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_manager/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_manager/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_manager/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_manager/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

