from django.urls import path

from ARTYapp import views

app_name='ARTYapp'
urlpatterns = [
    path('', views.index, name='Home'),
    path('profiles', views.profile, name='Profesors'),
    # path('courses', views.courses, name='course-list'),
    path('projects', views.project, name='Projects'),
    path('stock', views.stock, name='Stock'),
    # path('formHTML', views.form_hmtl),
    # path('course-django-forms', views.course_forms_django, name='CourseDjangoForms'),
    path('profile-django-forms', views.profile_forms_django, name='ProfileDjangoForms'),
    path('profile/<int:pk>/update', views.update_profile, name='UpdateProfile'),
    path('profile/<int:pk>/delete', views.delete_profile, name='DeleteProfile'),
    path('stock-django-forms', views.stock_forms_django, name='StockDjangoForms'),
    # path('search', views.search, name='Search'),


    # Dajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
    # from django.urls import path
    # from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    # urlpatterns = [
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.

   # path('courses', views.CourseListView.as_view(), name='course-list'),
   # path('course/add/', views.CourseCreateView.as_view(), name='course-add'),
   # path('course/<int:pk>/detail', views.CourseDetailView.as_view(), name='course-detail'),
   # path('course/<int:pk>/update', views.CourseUpdateView.as_view(), name='course-update'),
   # path('course/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course-delete'),
]
