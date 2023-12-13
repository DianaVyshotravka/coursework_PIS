from django.urls import path, include
from .views import new, index

app_name = 'reports'
urlpatterns = [
    path('reports', index, name='reports'),
    path('new', new, name='new')
]
