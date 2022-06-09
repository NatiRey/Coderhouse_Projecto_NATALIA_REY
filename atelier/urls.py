from django.urls import path

from atelier import views


app_name='atelier'
urlpatterns = [
    path('atelier', views.AtelierListView.as_view(), name='atelier-list'),
    path('atelier/add/', views.AtelierCreateView.as_view(), name='atelier-add'),
    path('atelier/<int:pk>/detail', views.AtelierDetailView.as_view(), name='atelier-detail'),
    path('atelier/<int:pk>/update', views.AtelierUpdateView.as_view(), name='atelier-update'),
    path('atelier/<int:pk>/delete', views.AtelierDeleteView.as_view(), name='atelier-delete'),
]
