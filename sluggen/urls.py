from django.urls import path

from sluggen import views

urlpatterns = [
    path('slugs/', views.SlugList.as_view()),
    path('create/', views.SlugCreate.as_view(), name='slug-create'),
]
