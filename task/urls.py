from django.urls import path, include
from .views import*
urlpatterns = [
    path('task-list/',task_list,name="task_list"),
    path('add-task/',add_task,name="add_task"),
    path('edit-task/<int:id>/',edit_task,name="edit_task"),
    path('delete-task/<int:id>/',delete_task,name="delete_task"),
    path('task-view/<int:id>/',task_view,name="task_view"),
    
    path('delete-task-image/<int:id>/',delete_task_image,name="delete_task_image"),
    path('task-submition/<int:id>/',task_submition,name="task_submition"), 

    path('api-view/',API_view,name="api_view"), 
    path('api-view/<int:id>/',API_view,name="api_view"), 

]