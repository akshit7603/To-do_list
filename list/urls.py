
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.task_list,name='home'),
    path('add_task/',views.add_task,name="task_add")
]
