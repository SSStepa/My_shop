from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (
    PermissionsMixin,
    UserManager,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from mptt.models import (
    MPTTModel,
    TreeForeignKey,
)


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class CategoryModel(MPTTModel, models.Model):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    type = models.CharField(max_length=50, null=True)

    class MPTTMeta:
        order_insertion_by = ["type", "name"]

    def __str__(self):
        return f"{self.pk}. {self.name}"


class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    cast = models.CharField(max_length=50, null=True, blank=True)
    time = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to="./images")

    def __str__(self):
        return f"{self.pk}. {self.name}"

    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={"product_id": self.pk})


class BlockedIPModel(models.Model):
    ip_name = models.CharField(max_length=25)


class URLFromModel(models.Model):
    url_from = models.URLField(help_text="url, from which you are going")
    url_to = models.URLField(help_text="url, which you are going to visit")
