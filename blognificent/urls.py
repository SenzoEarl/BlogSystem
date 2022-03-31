from django.urls import path

from blognificent import views

app_name = 'blognificent'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('details/<int:pk>', views.detail, name='detail'),
    path('<category>/', views.categories, name='category'),
]
