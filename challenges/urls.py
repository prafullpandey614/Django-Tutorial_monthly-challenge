from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.index , name="index"),
    path("<int:month>", views.challenges_by_number),
    path("<str:month>",views.monthly_challenge, name="monthly-challenge"),
]
