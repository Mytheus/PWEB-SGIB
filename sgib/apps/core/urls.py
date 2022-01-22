from django.urls import path
from sgib.apps.core import views

urlpatterns = [
    path('', views.do_login, name='login'),
    path('login/', views.do_login, name='login')
]
