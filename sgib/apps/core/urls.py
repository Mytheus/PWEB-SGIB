from django.urls import path
from sgib.apps.core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.do_login, name='login')
]
