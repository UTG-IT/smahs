from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.corecode.current_user import get_current_user

from .models import Staff


@receiver(pre_save, sender=Staff)
def staff_pre_save(sender, instance, **kwargs):
    # This signal runs before a Staff is saved.
    if not instance.pk:
        instance.created_by = get_current_user()
    instance.updated_by = get_current_user()



