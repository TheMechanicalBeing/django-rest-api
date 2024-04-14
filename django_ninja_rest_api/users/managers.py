from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_author', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        if extra_fields.get('is_author') is not True:
            raise ValueError(_("Author must have is_author=True"))

        return self.create_user(email, password, **extra_fields)
