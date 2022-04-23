import re
from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(_("username"), max_length=255, unique=True,
        help_text=_("Required. 30 characters or fewer. Letters, numbers and "
                    "/./-/_ characters"),
        validators=[
            validators.RegexValidator(re.compile(r"^[\w.-]+$"), _("Enter a valid username."), "invalid")
        ])
    email = models.EmailField(_("email address"), max_length=255, null=False, blank=False, unique=True)
    is_active = models.BooleanField(_("active"), default=True,
        help_text=_("Designates whether this user should be treated as "
                    "active. Unselect this instead of deleting accounts."))
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    full_name = models.CharField(_("full name"), max_length=256, blank=True)    

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["username"]    
