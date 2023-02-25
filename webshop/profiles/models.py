from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class ProfileManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Benutzer muss Emailadresse haben')

        if not username:
            raise ValueError('Benutzer muss username haben')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(blank=True, max_length=50)
    is_admin = models.BooleanField(default=False)
    # change this to false before shipping
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = ProfileManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class User_Delivery_Address(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    delivery_street = models.CharField(blank=True, max_length=100)
    delivery_house_number = models.CharField(blank=True, max_length=5)
    delivery_city = models.CharField(blank=True, max_length=100)
    delivery_zip_code = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return self.user.first_name


class User_Payment_Address(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    payment_street = models.CharField(blank=True, max_length=100)
    payment_house_number = models.CharField(blank=True, max_length=5)
    payment_city = models.CharField(blank=True, max_length=100)
    payment_zip_code = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return self.user.first_name


class User_Credit_Card(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    owner_first_name = models.CharField(blank=True, max_length=100)
    owner_last_name = models.CharField(blank=True, max_length=100)
    card_number = models.CharField(blank=True, max_length=100)
    expiration_date_month = models.CharField(blank=True, max_length=2)
    expiration_date_year = models.CharField(blank=True, max_length=2)
    security_code = models.CharField(blank=True, max_length=3)

    def __str__(self):
        return self.user.first_name


class User_PayPal(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    paypal_mail = models.CharField(blank=True, max_length=100)
    paypal_password = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.user.first_name


class User_Debit(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    debit_first_name = models.CharField(blank=True, max_length=100)
    debit_last_name = models.CharField(blank=True, max_length=100)
    iban = models.CharField(blank=True, max_length=22)
    bic = models.CharField(blank=True, max_length=11)

    def __str__(self):
        return self.user.first_name
