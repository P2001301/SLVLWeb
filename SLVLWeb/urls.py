from django.urls import path
from django.urls import path, include
from . import views # the “.” means current directory

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),
        path('user/', include('user.urls')),
]
