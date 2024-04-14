from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(email="any@user.com", password="pass")

        self.assertEqual(user.email, "any@user.com")
        self.assertFalse(user.is_author)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            user_model.objects.create_user()

        with self.assertRaises(TypeError):
            user_model.objects.create_user(email="")

        with self.assertRaises(ValueError):
            user_model.objects.create_user(email="", password="pass")

    def test_create_superuser(self):
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser(email="super@user.com", password="pass")

        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_author)

        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            user_model.objects.create_superuser(email="super@user.com", password="pass", is_superuser=False)
