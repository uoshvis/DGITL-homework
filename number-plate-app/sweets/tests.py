from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse

from sweets.models import SweetsData


class SweetsDataAPITestCase(APITestCase):

    def setUp(self):
        SweetsData.objects.create(
            name='Pupa',
            weight_grams=100,
            kcal=400,
        )

    def test_single_sweet(self):
        sweet_count = SweetsData.objects.count()
        self.assertEqual(sweet_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse('api-sweets:sweet-listcreate')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_item(self):
        data = {'name': 'Cake', 'weight_grams': 500, 'kcal': 4000}
        url = api_reverse('api-sweets:sweet-listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        # test the get item
        sweet = SweetsData.objects.first()
        data = {}
        url = sweet.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        sweet = SweetsData.objects.first()
        url = sweet.get_api_url()
        data = {'name': 'Pupa', 'kcal': 399, 'weight_grams': 100}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_delete_item(self):
        sweet = SweetsData.objects.first()
        url = sweet.get_api_url()
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        sweet_count = SweetsData.objects.count()
        self.assertEqual(sweet_count, 0)
