from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status


class BonosTestCase(TestCase):
    def setUp(self):
        user = User(
            username='testuser',
            email='testuser@localhost.com'
        )
        user.set_password('testpassword')
        user.save()

    def test_create_bono(self):

        client = APIClient()
        client.login(username='testuser', password='testpassword')
        response = client.get('/bonos/')
        counter = response.json().get('count')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(counter, 0)
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'testbono01',
                'bono_number': '1200',
                'bono_price': '1200'
            }
        )
        bono_name = response.json().get('bono_name')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bono_name, 'testbono01')
        response = client.get('/bonos/')
        counter = response.json().get('count')
        self.assertEqual(counter, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_name_validator(self):

        client = APIClient()
        client.login(username='testuser', password='testpassword')
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'te',
                'bono_number': '1200',
                'bono_price': '1200'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {"bono_name": ["Ensure this field has at least 3 characters."]})
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'M' * 41,
                'bono_number': '1200',
                'bono_price': '1200'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {"bono_name":["Ensure this field has no more than 40 characters."]})
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'tes',
                'bono_number': '1200',
                'bono_price': '1200'
            }
        )
        bono_name = response.json().get('bono_name')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bono_name, 'tes')
        response = client.post(
            '/bonos/',
            {
                'bono_name': 't' * 39,
                'bono_number': '1200',
                'bono_price': '1200'
            }
        )
        bono_name = response.json().get('bono_name')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bono_name, 't' * 39)

    def test_number_of_bonds_validator(self):

        client = APIClient()
        client.login(username='testuser', password='testpassword')
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'test_number_bonds_fail',
                'bono_number': '0',
                'bono_price': '1200'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {"bono_number":["Ensure this value is greater than or equal to 1."]})
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'test_number_bonds_fail',
                'bono_number': '10001',
                'bono_price': '1200'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {"bono_number":["Ensure this value is less than or equal to 10000."]})

        response = client.post(
            '/bonos/',
            {
                'bono_name': 'tnbs01',
                'bono_number': '1',
                'bono_price': '1200'
            }
        )
        bono_name = response.json().get('bono_name')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bono_name, 'tnbs01')

        response = client.post(
            '/bonos/',
            {
                'bono_name': 'tnbs02',
                'bono_number': '10000',
                'bono_price': '1200'
            }
        )
        bono_name = response.json().get('bono_name')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bono_name, 'tnbs02')

    def test_selling_price_validator(self):

        client = APIClient()
        client.login(username='testuser', password='testpassword')
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'test_sp_fail',
                'bono_number': '1',
                'bono_price': '-1'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'bono_price': ['Ensure this value is greater than or equal to 0.']})
        response = client.post(
            '/bonos/',
            {
                'bono_name': 'test_sp_fail',
                'bono_number': '1',
                'bono_price': '100000001'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'bono_price': ['Ensure this value is less than or equal to 100000000.']})

        response = client.post(
            '/bonos/',
            {
                'bono_name': 'tnsp01',
                'bono_number': '1',
                'bono_price': '0'
            }
        )
        bono_name = response.json().get('bono_name')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bono_name, 'tnsp01')

        response = client.post(
            '/bonos/',
            {
                'bono_name': 'tnsp02',
                'bono_number': '10000',
                'bono_price': '100000000'
            }
        )
        bono_name = response.json().get('bono_name')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bono_name, 'tnsp02')

        # print(response.content)
        # print(response.status_code)
