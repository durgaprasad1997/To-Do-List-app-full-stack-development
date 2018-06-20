from django.views import View
from TodoApp.models import *
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.forms import ModelForm
from django import forms
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate


class AddTask(forms.ModelForm):
    class Meta:
        model=todoapp
        exclude=['id','user']
        widgets={
            'name':forms.TextInput(),
            'type':forms.TextInput(),
            'start_date':forms.TextInput(),
            'end_date':forms.TextInput(),
            'description':forms.TextInput(),
        }
class Viewtasklist(LoginRequiredMixin,ListView):
    model=todoapp
    context_object_name = 'tasks'
    template_name = 'task_list.html'

    def get_object(self,queryset=None):
        return get_object_or_404(todoapp,**self.kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(Viewtasklist,self).get_context_data(**kwargs)
        context['cards']=self.model.objects.filter(user=self.request.user).values()
        context.update({'user_permissions':self.request.user.get_all_permissions})
        return context


class AddTaskView(LoginRequiredMixin,CreateView):
    template_name = 'create_task.html'
    model = todoapp
    form_class = AddTask
    success_url = reverse_lazy('index.html')
    # import ipdb
    # ipdb.set_trace()
    def get_context_data(self, **kwargs):
        context = super(AddTaskView, self).get_context_data(**kwargs)
        context.update({
            'form': context.get('form'),
            'user_permissions': self.request.user.get_all_permissions()
        })
        return context

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('user_id'))
        userform = AddTask(request.POST)

        if userform.is_valid():
          card = userform.save(commit=False)
          card.user=user
          card.save()
        return redirect('/tasklist/')

class UpdateTask(LoginRequiredMixin,UpdateView):
    model=todoapp
    template_name = 'create_task.html'
    form_class = AddTask
    success_url = reverse_lazy('tasklist')

class DeleteTask(LoginRequiredMixin,DeleteView):
    model = todoapp
    template_name = 'delete_confirm.html'
    form_class=AddTask
    success_url = reverse_lazy('tasklist')


