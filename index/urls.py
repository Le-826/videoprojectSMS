from django.urls import path

from index import views

urlpatterns = [
    path('css/', views.index)
]