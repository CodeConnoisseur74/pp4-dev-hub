from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile



#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        member = instance
        profile = Profile.objects.create(
            member=member,
            username=member.username,
            email=member.email,
            name=member.first_name,
            )

def deleteMember(sender, instance, **kwargs):
    member = instance.member
    member.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteMember, sender=Profile)