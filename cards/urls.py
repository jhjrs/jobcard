from django.urls import path
from cards.views import job_card_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/', views.job_card_view, name='card'),
    path('login/', views.login_view, name='login'),
    path('register/', views.registration_view, name='register'),

]