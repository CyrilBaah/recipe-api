"""
Test for User model
"""
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successfull(self):
        """Test creating a user with email is successful"""
        email = "test@example.com"
        password = "testpassword123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.password, password)

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@EXAMPLE.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without email raises a ValueError exception"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
