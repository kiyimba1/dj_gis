from django.urls import path

from location.views import HotelUpdateRetrieveView, ListCreateGenericViews

urlpatterns = [
    path("hotels", ListCreateGenericViews.as_view()),
    path("hotels/<str:pk>", HotelUpdateRetrieveView.as_view())
]
