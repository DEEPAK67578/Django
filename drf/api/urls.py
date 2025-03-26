from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.api_home),
    #apidecorator
    path("apidecorator/",views.descoratorAPIVIEW),
    path("apidecoratorv2/",views.decoratorAPIViewV2)
]