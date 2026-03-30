from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index,name='index'),
    path('', views.index),
    path('createStudent',views.createStudent),
    path('delete-student/<int:sid>/',views.deleteStudent),

    # path('update-form/<int:sid>/',views.updateForm),
    path('update-form/<int:sid>/',views.updateFormData)
     
]