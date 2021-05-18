from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

import uuid 

#https://noumenon-th.net/programming/2019/12/13/abstractbaseuser/ sanyou



#ここ( https://github.com/django/django/blob/master/django/contrib/auth/models.py#L321 )から流用
class CustomUser(AbstractBaseUser, PermissionsMixin):

    #username_validator  = UnicodeUsernameValidator()
    '''
    #id - UUID
    #email
    #password
    #handle_name
    #phone_number
    #status
    '''
    id          = models.UUIDField( default=uuid.uuid4, primary_key=True, editable=False )

    handle_name = models.CharField(verbose_name="handle_name", max_length=20)
    email       = models.EmailField(_('email address'),max_length=255,unique=True,error_messages={'unique': _("A user with that username already exists."),},
    )
    #!!!phonenumber varidate only[number]
    phonenumber = models.CharField(verbose_name="phonenumber",max_length=11,)

    status      = models.IntegerField(verbose_name="status",default=0,blank=False)

    is_staff    = models.BooleanField(
                    _('staff status'),
                    default=False,
                    help_text=_('Designates whether the user can log into this admin site.'),
                )

    is_active   = models.BooleanField(
                    _('active'),
                    default=True,
                    help_text=_(
                        'Designates whether this user should be treated as active. '
                        'Unselect this instead of deleting accounts.'
                    ),
                )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects     = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['handle_name','phonenumber']

    class Meta:
        verbose_name        = _('user')
        verbose_name_plural = _('users')
        #abstract            = True

    def clean(self):
        super().clean()
        self.email  = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        return self.handle_name

    def get_short_name(self):
        return self.handle_name