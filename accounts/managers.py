from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError('User must have an username.')
        if not first_name and last_name:
            raise ValueError('User must have a first name and a last name.')

        user = self.model(username=username, first_name=first_name,
                          last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError('User must have an username.')
        if not first_name and last_name:
            raise ValueError('User must have a first name and a last name.')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(username=username, first_name=first_name,
                          last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    class Meta:
        abstract = True
