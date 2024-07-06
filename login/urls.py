from django.urls import include, path
from .views import login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', include('dashboard.urls')),
]
