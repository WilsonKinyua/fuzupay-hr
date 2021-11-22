from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.superadmin.models import *




@receiver(post_save, sender=User)
def create_associate_tables(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(employee=instance)
        # EmploymentInformation.objects.create(employee=instance)
        # PaymentInformation.objects.create(employee=instance)
        # EmergencyInformation.objects.create(employee=instance)

try:
    if len(Role.objects.all()) < 3:
        Role.objects.create(name="super_admin")
        Role.objects.create(name="human_resources")
        Role.objects.create(name="subordinate_staff")
except:
    print("Roles does not exist yet")
