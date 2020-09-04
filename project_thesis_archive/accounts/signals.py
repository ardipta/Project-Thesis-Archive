from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from accounts.models import StudentProfile

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def create_student_profile(sender, **kwargs):
    if kwargs['created']:
        StudentProfile.objects.created(user=kwargs['instance'])

    post_save.connect(create_student_profile, sender=User)
