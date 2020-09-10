# Web-browsable Web API using Django and Django REST framework

The project builds a simple user database. There are two endpoints `/customer` and `/reservations` which allow Retrieve, List, Create, Update, and Delete a Customer or Reservation. <br />
The permission of Create, Update, and Delete is set for admin and staff. A normal user can only List and Retrieve on API.

### Development

Run the project within the project directory:

```
python manage.py runserver
```

### Test

The tests for the Create and List for a normal user and a staff:

```
python manage.py test
```
