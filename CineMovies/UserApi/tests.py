from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory


# Create your tests here.

class UserModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@email.com")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertFalse(self.user.is_staff)

    def authenticate_user(self):
        authenticated = self.client.login(username="testuser",
                                          password="testpassword"
                                          )
        self.assertTrue(authenticated)

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), "testuser")


class CreateAdminUserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            username="testadminuser",
            email="testadmin@email.com",
            password="testpassword",
            is_staff=True)

    def test_admin_creation(self):
        self.assertEqual(self.user.username, "testadminuser")
        self.assertEqual(self.user.email, "testadmin@email.com")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertTrue(self.user.is_staff)

    def test_admin_authentication(self):
        authenticated = self.client.login(
            username="testadminuser",
            password="testpassword")

        self.assertTrue(authenticated)


class UserModelApiTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
        )

    def GetTokenView(self):
        self.data = {
            'username': "testuser",
            "password": "testpassword",
        }
        response = self.client.post(path="/api/token", data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

