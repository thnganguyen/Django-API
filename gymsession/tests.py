import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from gymsession.models import Customer, Reservation

class CustomerModelAuthTests(APITestCase):
    client = APIClient()
    url_customer = reverse('customer-list')
    data_customer = {
            'first_name': 'firstname_test',
            'last_name':'lastname_test',
            'email': 'email@test.com'
    }
    
    def setUp(self):
        # create user
        User.objects.create_user(username='test_user', password='password123')
        self.client.login(username='test_user', password='password123')

    def test_post_customer(self):
        response = self.client.post(self.url_customer, self.data_customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, 'firstname_test')
        self.assertEqual(Customer.objects.get().last_name, 'lastname_test')
        self.assertEqual(Customer.objects.get().email, 'email@test.com')

    def test_list_customer(self):
        self.client.post(self.url_customer, self.data_customer, format='json')
        response = self.client.get(self.url_customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_detail_customer(self):
        self.client.post(self.url_customer, self.data_customer, format='json')
        response = self.client.get(reverse('customer-detail', args=(1,)), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], 'lastname_test')

    def test_list_no_customer(self):
        response = self.client.get(self.url_customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_detail_no_customer(self):
        response = self.client.get(reverse('customer-detail', args=(1,)), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CustomerModelNoAuthTests(APITestCase):
    client = APIClient()
    url_customer = reverse('customer-list')
    data_customer = {
        'first_name': 'firstname_test',
            'last_name':'lastname_test',
            'email': 'email@test.com'
    }

    def test_list_customer_no_auth(self):
        response = self.client.get(self.url_customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_no_customer_no_auth(self):
        response = self.client.get(reverse('customer-detail', args=(1,)), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_customer_no_auth(self):
        response = self.client.post(self.url_customer, self.data_customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReservationModelAuthTests(APITestCase):
    client = APIClient()
    url_reservation = reverse('reservation-list')
    time = timezone.now() + datetime.timedelta(days=5)
    data_reservation = {
        'name': 'name_test',
        'reservation_date': time
    }

    def setUp(self):
        # create user
        User.objects.create_user(username='test_user', password='password123')
        self.client.login(username='test_user', password='password123')

    def test_post_reservation(self):
        response = self.client.post(self.url_reservation, self.data_reservation, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_reservation(self):
        self.client.post(self.url_reservation, self.data_reservation, format='json')
        response = self.client.get(self.url_reservation, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_reservation(self):
        self.client.post(self.url_reservation, self.data_reservation, format='json')
        response = self.client.get(reverse('reservation-detail', args=(1,)), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'name_test')
    
    def test_list_no_reservation(self):
        response = self.client.get(self.url_reservation, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
    
    def test_detail_no_reservation(self):
        response = self.client.get(reverse('reservation-detail', args=(1,)), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ReservationModelNoAuthTests(APITestCase):
    client = APIClient()
    url_reservation = reverse('reservation-list')
    time = timezone.now() + datetime.timedelta(days=5)
    data_reservation = {
        'name': 'name_test',
        'reservation_date': time
    }

    def test_list_reservation_no_auth(self):
        response = self.client.get(self.url_reservation, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_detail_no_reservation_no_auth(self):
        response = self.client.get(reverse('reservation-detail', args=(1,)), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_post_reservation_no_auth(self):
        response = self.client.post(self.url_reservation, self.data_reservation, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
