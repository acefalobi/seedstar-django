from django.urls import path

from profile_app import views

urlpatterns = [
    path('', views.landing_page),
    path('add', views.add_profile),
    path('list', views.list_profile)
]