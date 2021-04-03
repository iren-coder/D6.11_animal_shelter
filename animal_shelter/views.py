from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Animal, Employee
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render


class HomePageView(TemplateView):

    template_name = "home.html"

    # def get_animal(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["latest_articles"] = Animal.objects.all()
    #     return context

class EmployeeView(ListView):
    model = Employee
    template_name = 'employee.html'
    context_object_name = "employee"

def employee_list(request):
    employees = Employee.objects.all()
    return HttpResponse(employees)

def employee(request):
    template = loader.get_template('employee.html')
    employees = Employee.objects.all()
    employees_data = {
        "title": "сотдрудники",
        "employees": employees,
    }
    return HttpResponse(template.render(employees_data, request))

class CatsList(ListView):
    queryset = Animal.objects.filter(kind_of_animal='C')
    template_name = "pets.html"
    context_object_name = "pets"


class DogsList(ListView):
    queryset = Animal.objects.filter(kind_of_animal='D')
    template_name = "pets.html"
    context_object_name = "pets"


class ParrotsList(ListView):
    queryset = Animal.objects.filter(kind_of_animal='P')
    template_name = "pets.html"
    context_object_name = "pets"


class ContactsPageView(TemplateView):
    template_name = "contacts.html"


class CatDetailView(DetailView):
    # queryset = Animal.objects.filter(kind_of_animal='C')
    model = Animal
    template_name = "pet_info.html"
    context_object_name = "pet"


