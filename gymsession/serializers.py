from rest_framework import serializers
from gymsession.models import Customer, Reservation


class CustomerRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['url', 'id', 'first_name', 'last_name', 'email', 'phone']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['url', 'id', 'name', 'reservation_date', 'address']
