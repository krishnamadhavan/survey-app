import binascii
import os

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Token(models.Model):
    key = models.CharField(_('Key'), max_length=40, primary_key=True, help_text=_('Auth token of the user.'))
    user = models.ForeignKey(to=User, related_name='auth_tokens', on_delete=models.CASCADE)
    uuid = models.CharField(_('UUID'), max_length=255, help_text=_('Unique identifier for a client device.'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        db_table = _('auth_tokens')
        verbose_name = _('Auth token')
        verbose_name_plural = _('Auth tokens')
        unique_together = ('user', 'uuid',)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.key:
            self.key = self.generate_key
        super(Token, self).save()

    @property
    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
        return u'{0} (client: {1})'.format(self.key, self.uuid)

    LOGIN_FIELDS = (
        'uuid',
    )
