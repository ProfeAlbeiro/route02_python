from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name="contact"),
    path('create/', views.create, name="contact_create"),
    path('view/<int:id>', views.view, name="contact_view"),
    path('edit/<int:id>', views.edit, name="contact_edit"),
    path('delete/<int:id>', views.delete, name="contact_delete"),
]