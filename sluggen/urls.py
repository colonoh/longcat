from django.urls import path

from sluggen import views

urlpatterns = [
    path('slugs/', views.slug_list),
    path('slugs/<int:pk>/', views.slug_details),
]
