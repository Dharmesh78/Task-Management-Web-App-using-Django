from django.urls import path
from taskApp import views
from django.conf import settings # new

from django.conf.urls.static import static

#TEMPLATE URLs
app_name='taskApp'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('addTaskHandle/',views.add_task,name='addTask'),
    path('myTasks/',views.my_task,name='myTask'),
    path('toggle/', views.toggle,name='toggle'),
    path('editTask/<task_id>',views.edit,name='edit'),
    path('deleteTask/<task_id>',views.delete_task,name='delete'),
]
