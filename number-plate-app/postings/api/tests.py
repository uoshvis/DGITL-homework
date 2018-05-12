from rest_framework.test import APITestCase
from rest_framework import status

from rest_framework_jwt.settings import api_settings

from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from postings.models import BlogPost

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class BlogPostAPITestCase(APITestCase):

    def setUp(self):
        user_obj = User.objects.create(
            username='testuser',
            email='email@mail.com'
        )
        user_obj.set_password('qwerrty123')
        user_obj.save()
        BlogPost.objects.create(
            user=user_obj,
            title='New title',
            content='Awesome'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count, 1)

    def test_get_list(self):
        # test the get list
        data = {}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item(self):
        # test the post item unauthorized
        data = {'title': 'Good day', 'content': 'Hello again'}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        # test the get item
        blog_post = BlogPost.objects.first()
        data = {}
        url = blog_post.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        # test the update item unauthorized
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {'title': 'Good dayagin', 'content': 'Hello again'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_item_auth(self):
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {'title': 'Good dayagin', 'content': 'Hello again'}
        user_obj = User.objects.first()
        payload = jwt_payload_handler(user_obj)
        token_rsp = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_auth(self):
        user_obj = User.objects.first()
        payload = jwt_payload_handler(user_obj)
        token_rsp = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>
        data = {'title': 'Good day', 'content': 'Hello again'}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_ownership(self):
        owner = User.objects.create(username='testuserNext')
        blog_post = BlogPost.objects.create(
            user=owner,
            title='New title',
            content='Awesome'
        )
        user_obj = User.objects.first()
        self.assertNotEqual(user_obj.username, owner.username)

        payload = jwt_payload_handler(user_obj)
        token_rsp = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>

        url = blog_post.get_api_url()
        data = {'title': 'Good dayagin', 'content': 'Hello again'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_login(self):
        data = {
            'username': 'testuser',
            'password': 'qwerrty123'
        }
        url = api_reverse('api-login')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token')
        if token is not None:
            blog_post = BlogPost.objects.first()
            url = blog_post.get_api_url()
            data = {'title': 'Good dayagin', 'content': 'Hello again'}
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

# request.post(url, data, headers={"Authorization": "JWT" + <token>})
