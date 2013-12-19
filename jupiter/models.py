from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.conf import settings

class Reading(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  reading = models.DecimalField(max_digits=5, decimal_places=2)
  when = models.DateTimeField(auto_now_add=True)

  READING_TYPES = (
    ('WGHT', 'Weight'),
    ('HEHT', 'Height'),
    ('BLSG', 'Blood Sugar'),
    ('PLSE', 'Pulse'),
    ('BPRS', 'Blood Pressure'),
  )

  type = models.CharField(max_length=4, choices=READING_TYPES)

  def get_absolute_url(self):
    return reverse('user_detail')

class User(AbstractUser):
  # True = Female, False = Male
  sex = models.NullBooleanField(null=True, blank=True)

  history = models.NullBooleanField(null=True, blank=True)

  ETHNICITY_OPTIONS = (
    ('WHT', 'White'),
    ('AFA', 'African American'),
    ('API', 'Asian/Pacific Islanders'),
    ('NA', 'Native American'),
    ('HIS', 'Hispanic/Latino'),
    ('OT', 'Other'),
  )
  ethnicity = models.CharField(max_length=4, choices=ETHNICITY_OPTIONS, null=True, blank=True)

  history_blood_pressure = models.NullBooleanField(null=True, blank=True)

  physically_active = models.NullBooleanField(null=True, blank=True)

  def get_absolute_url(self):
    return reverse('user_detail')


