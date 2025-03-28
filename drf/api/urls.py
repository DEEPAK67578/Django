from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.api_home),
    #apidecorator
    path("apidecorator/",views.descoratorAPIVIEW),
    path("apidecoratorv2/",views.decoratorAPIViewV2),
    path("genericCreateView/",views.DummyCreateGenericVIew.as_view()),
    path("genericRetrieveView/<int:pk>",views.DummyRetrieveGenericView.as_view()),
    path("genericListView/",views.DummyListGenericView.as_view()),
    path('genericUpdateView/<int:pk>/',views.DummyUpdateGenericView.as_view()),
    path('genericDeleteView/<int:pk>/',views.DummyDeleteGenericView.as_view()),
    path('customgenericView/',views.CustomGenericView.as_view()),

    path('customgenericView/<int:pk>',views.CustomGenericView.as_view())
]