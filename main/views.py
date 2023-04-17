from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *

# Create your views here.


def companies_view(request):
    return render(request, 'companies.html', {"companies": Company.objects.all()})


def associate_employee(request, company_id):
    company = Company.objects.get(pk=company_id)
    employees = Employee.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = Employee.objects.get(pk=employee_id)
        employee.company = company
        employee.save()
        return redirect('/')
    return render(request, 'associate_employee.html', {'company': company, 'employees': employees})

