from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class CustomUserTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username='petko',
            email='petko@gmail.com',
            password='pass123'
        )

        self.assertEqual(user.username, 'petko')
        self.assertEqual(user.email, 'petko@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='admin123'
        )

        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)