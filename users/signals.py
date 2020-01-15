from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# below are for automatically setting default image to user profile when they have created.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kewargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kewargs):
    instance.profile.save()