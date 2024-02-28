from django.urls import path
from cards.views import job_card_view
from . import views
from .views import display_users
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('job/', views.job_card_view, name='card'),
    path('login/', views.login_view, name='login'),
    path('register/', views.registration_view, name='register'),
    path('users/', display_users, name='display_users'),
    path('photos/', views.display_photos, name='display_photos'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
