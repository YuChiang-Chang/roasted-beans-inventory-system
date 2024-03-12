from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CustomPermission

@receiver(post_save, sender=CustomPermission)
def assign_permission_to_superusers(sender, instance, created, **kwargs):
    if created:
        User = get_user_model()
        superusers = User.objects.filter(is_superuser=True)
        for user in superusers:
            user.permissions.add(instance)