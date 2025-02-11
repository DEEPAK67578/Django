from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.resToMonthNum),
    path("<str:month>", views.resToMonth,name="month-challenge"),
]
