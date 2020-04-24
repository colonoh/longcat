from django.urls import path

from sluggen import views

urlpatterns = [
    path('api/v1/slugs/', views.SlugList.as_view()),
    path('api/v1/create/', views.SlugCreate.as_view(), name='slug-create'),
    path('<slug>/', views.redirect_view),
]
