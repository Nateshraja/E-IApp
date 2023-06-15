from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_installment/', views.add_installment, name='add_installment'),
    path('report/', views.generate_report, name='report'),
    path('', views.home, name='home'),
    path('expense/<int:pk>/edit/', views.edit_expense, name='edit_expense'),
    path('expense/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
    path('installment/<int:pk>/edit/', views.edit_installment, name='edit_installment'),
    path('installment/<int:pk>/delete/', views.delete_installment, name='delete_installment'),
]
