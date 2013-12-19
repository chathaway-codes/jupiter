from django.db import models
from django.contrib.auth.models import AbstractUser

class Reading(models.Model):
  reading = models.DecimalField(max_digits=5, decimal_places=2)
  when = models.DateTimeField(auto_now_add=True)

  READING_TYPES = (
    ('WGHT', 'Weight'),
    ('HEHT', 'Height'),
    ('BLSG', 'Blood Sugar'),
    ('PLSE', 'Pulse'),
    ('BPRS', 'Blood Pressure'),
  )

  type = models.CharField(length=4, choices=READING_TYPES)

class User(AbstractUser):
  # True = Female, False = Male
  sex = models.BooleanField()

  history = models.BooleanField()

  ETHNICITY_OPTIONS = (
    ('WHT', 'White'),
    ('AFA', 'African American'),
    ('API', 'Asian/Pacific Islanders'),
    ('NA', 'Native American'),
    ('HIS', 'Hispanic/Latino'),
    ('OT', 'Other'),
  )
  ethnicity = models.CharField(length=4, choices=ETHNICITY_OPTIONS)

  history_blood_pressure = models.BooleanField()

  physically_active = models.BooleanField()


