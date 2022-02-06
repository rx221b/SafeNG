from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sanitize',views.sanitize,name='sanitize'),
    path('safecheckwebsite',views.safecheckwebsite,name='safecheckwebsite')
]


