from gymsession.models import Customer, Reservation
from gymsession.serializers import CustomerRegistrationSerializer, ReservationSerializer

from rest_framework import viewsets
from rest_framework import permissions


class CustomerRegistrationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Customer.objects.all()
    serializer_class = CustomerRegistrationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
