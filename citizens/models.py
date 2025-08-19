from django.db import models
from datetime import datetime
import re
from django.core.exceptions import ValidationError
# Create your models here.
class Citizen(models.Model):
    national_id = models.CharField(primary_key=True, max_length=14)
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"birth_date: {self.birth_date}, birth_place: {self.birth_place}"
    def clean(self):
        try:
            self.validate_national_id(self.national_id)
        except ValueError as e:
            raise ValidationError({'national_id': str(e)})
        
    def save(self, *args, **kwargs):
        self.full_clean()  # This calls clean() and validates the model
        if self.national_id and (self.birth_date is None or self.birth_place is None):
            self.birth_date, self.birth_place = self.extract_birth_info(self.national_id)
        super().save(*args, **kwargs)
    
    @staticmethod           
    def validate_national_id(value):
        if not re.match(r'^\d{14}$', value):
            raise ValueError("National ID must be exactly 14 digits.")
        if value[0] not in ['2', '3']:
            raise ValueError("National ID must start with 2 or 3.")
        try:
            century = 1900 if value[0] == '2' else 2000
            year = century + int(value[1:3])
            month = int(value[3:5])
            day = int(value[5:7])
            datetime(year, month, day)
        except ValueError:
            raise ValueError("National ID contains an invalid birth date.")
        return value

    @staticmethod
    def extract_birth_info(national_id):
        # Extract century
        century_digit = national_id[0]
        year = int(national_id[1:3])
        month = int(national_id[3:5])
        day = int(national_id[5:7])
        governorate_code = int(national_id[7:9])

        # Determine full year
        if century_digit == '2':
            year += 1900
        elif century_digit == '3':
            year += 2000
        else:
            raise ValueError("Invalid century digit in national ID.")

        # Validate date
        try:
            birth_date = datetime(year, month, day).date()
        except ValueError:
            raise ValueError("Invalid birth date in national ID.")

        return birth_date, governorate_code
