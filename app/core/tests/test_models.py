from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successful"""
        email = "thamz@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = "Thamz@GMAIL.COM"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email,  password)
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        "Test creating with no email raises error"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Pass123")

    def test_create_new_superuser(self):
        """Testing creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "thamz@gmail.com"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
