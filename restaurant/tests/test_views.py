from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(id=2, title="Greek Pasta", price=30.00, inventory=50)
        Menu.objects.create(id=3, title="Lemon Cake", price=50.00, inventory=200)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        

    def test_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)

        expected_data = [

            {'id': 2, 'title': 'Greek Pasta', 'price': '30.00', 'inventory': 50},
            {'id': 3, 'title': 'Lemon Cake', 'price': '50.00', 'inventory': 200},

        ]

        self.assertEqual(response.json(), expected_data)