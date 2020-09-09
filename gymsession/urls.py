from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gymsession import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'customer', views.CustomerRegistrationViewSet)
router.register(r'reservations', views.ReservationViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
               path('', include(router.urls)),
               ]

