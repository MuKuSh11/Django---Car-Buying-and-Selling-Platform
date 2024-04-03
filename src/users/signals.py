from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, Location

# signal that triggers after a user is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Profile object gets created when a user is created, not when it is edited
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created:
        # Location.objects.create(profile=instance)
        # because of OneToOneField in Profile for Location, vice-versa is also true, that Location will also have a Profile field too
        profile_location = Location.objects.create()
        instance.location = profile_location
        instance.save()