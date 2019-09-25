from django.urls import path

from . import views
# Create an 'all/' endpoint that prints out all entry names
urlpatterns = [
    path('', views.index, name='index'),
    path('book/add/', views.addBook),
    path('book/all/', views.allBook),
    path('book/',views.allBookPublishDates) #create a new endpoint that only prints entries with publish dates greater than or equal to 01/01/2018.
]