from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS


class TradersForm(ModelForm):
    headline = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text='Use puns liberally',
    )
    content = models.TextField()

    class Meta:
        model = Trader
        exclude = ('model_define',)

        labels = {
            'name': _('اسمك'),
            'model_define': _('حدد المنتج'),
            'telephone': _('رقم المحمول'),
            'email_facebook': _('حساب الالكترونى '),
            'address': _('عنوان'),
            'quentity': _('الكميه'),

        }
        help_texts = {
            'name_maker': _('ادخل اسمك'),
        }
        error_messages = {
            'name': {
                'null': _("ذلك الاسم متجوز الحد")
            }
        }
