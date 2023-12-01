from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
#from django.core.mail import send_mail
# from django.conf import settings


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            member=user,  # Changed from user to member
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        # ... send_mail functionality


@receiver(post_save, sender=Profile)
def updateMember(sender, instance, created, **kwargs):
    profile = instance
    member = profile.member  # Changed from user to member

    if not created:
        member.first_name = profile.name
        member.username = profile.username
        member.email = profile.email
        member.save()


@receiver(post_delete, sender=Profile)
def deleteMember(sender, instance, **kwargs):
    try:
        print("Deleting user...")
        member = instance.user
        member.delete()
    except User.DoesNotExist:
        print("User does not exist. This has to do with the relationship between User and Profile.")


post_save.connect(createProfile, sender=User)
post_save.connect(updateMember, sender=Profile)
post_delete.connect(deleteMember, sender=Profile)
