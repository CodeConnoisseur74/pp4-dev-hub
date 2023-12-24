from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            member=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = "Welcome to DevHub"
        message = "We are glad you are here!"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Profile)
def update_member(sender, instance, created, **kwargs):
    profile = instance
    member = profile.member

    if not created:
        member.first_name = profile.name
        member.username = profile.username
        member.email = profile.email
        member.save()


@receiver(post_delete, sender=Profile)
def delete_member(sender, instance, **kwargs):
    try:
        print("Deleting user...")
        user = instance.member
        user.delete()
    except User.DoesNotExist:
        print("User does not exist.")


post_save.connect(create_profile, sender=User)
post_save.connect(update_member, sender=Profile)
post_delete.connect(delete_member, sender=Profile)
