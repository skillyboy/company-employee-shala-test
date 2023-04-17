from django.urls import path

from main import views

# app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('associate_employee/<int:company_id>/', views.associate_employee, name='associate_employee'),
]
