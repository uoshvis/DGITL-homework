from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from carplates.models import CarPlate


class CarPlateTest(APITestCase):

    client = APIClient()

    link = '/api/carplates/'

    def setUp(self):
        self.carplates_data = []
        for i in range(5):
            self.carplates_data.append(CarPlate.objects.create(
                plate_number='HOT12' + str(i),
                first_name='Name' + str(i),
                last_name='Surname' + str(i)
            ))

    def tearDown(self):
        CarPlate.objects.all().delete()

    def test_list(self):
        response = self.client.get(self.link, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(self.carplates_data), len(response.data))

    def test_retrieve(self):
        self.link += str(self.carplates_data[0].id) + '/'
        response = self.client.get(self.link, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.carplates_data[0].id)

    def test_retrieve_not_found(self):
        self.link += str(self.carplates_data[-1].id + 1) + '/'
        response = self.client.get(self.link, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 1)

    def test_create(self):
        self.tearDown()
        data = {
            'plate_number': 'PPP777',
            'first_name': 'Kaliause',
            'last_name': 'Bekepuris'
        }
        response = self.client.post(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(CarPlate.objects.all()), 1)

    def test_create_invalid_field(self):
        self.tearDown()
        data = {
            'plate_number': 'aaa777',
            'boom': 'Kaliause',
            'last_name': 'Bekepuris'
        }
        response = self.client.post(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_lenght(self):
        self.tearDown()
        data = {
            'plate_number': 'P',
            'first_name': 'Kaliause',
            'last_name': 'Bekepuris'
        }
        response = self.client.post(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_letter(self):
        self.tearDown()
        data = {
            'plate_number': 'AAX150',
            'first_name': 'Kaliause',
            'last_name': 'Bekepuris'
        }
        response = self.client.post(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_number(self):
        self.tearDown()
        data = {
            'plate_number': 'AABAA1',
            'first_name': 'Kaliause',
            'last_name': 'Bekepuris'
        }
        response = self.client.post(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update(self):
        data = {
            'first_name': 'Majonezas',
            'last_name': 'Magnis',
            'id': 200,
        }
        self.link += str(self.carplates_data[0].id) + '/'
        response = self.client.put(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])
        self.assertNotEqual(response.data['id'], data['id'])

    def test_update_404(self):
        data = {
            'first_name': 'Majonezas',
            'last_name': 'Daumantu'
        }
        self.link += str(self.carplates_data[-1].id + 1) + '/'
        response = self.client.put(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 1)

    def test_update_plate_not_allowed(self):
        data = {
            'first_name': 'Majonezas',
            'last_name': 'Daumantu',
            'plate_number': 'TTT000'
        }
        self.link += str(self.carplates_data[0].id) + '/'
        response = self.client.put(self.link, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data), 1)

    def test_delete(self):
        self.link += str(self.carplates_data[0].id) + '/'
        response = self.client.delete(self.link, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete(self.link, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
