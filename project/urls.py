from django.urls import path

from project import views


app_name='project'
urlpatterns = [
    path('projects', views.project_list, name='project-list'),
    path('project/add', views.project_form, name='project-add'),
    path('project/<int:pk>/update', views.update_project, name='project-update'),
    path('project/<int:pk>/delete', views.delete_project, name='project-delete'),
]
