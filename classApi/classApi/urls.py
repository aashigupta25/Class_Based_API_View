from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person-api/', views.PersonAPI.as_view()),
    path('person-api/<int:pk>/', views.PersonAPI.as_view()),
]
