from django.urls import path
from .views import get_jobs,job_detail

urlpatterns = [
    path('jobs/',get_jobs, name = 'get_jobs'),
    path('jobs/<int:pk>/', job_detail, name='job_detail'),
    
]
