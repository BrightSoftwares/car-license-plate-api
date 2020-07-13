from django.core.validators import RegexValidator
from django.db import models


class Owner(models.Model):
    alphabetical = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetical letters are allowed.')

    name = models.CharField(max_length=20, blank=False, null=False, validators=[alphabetical])
    surname = models.CharField(max_length=20, blank=False, null=False, validators=[alphabetical])

    def total_plates(self):
        return self.plates.count()

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Plate(models.Model):
    # license_number_format = RegexValidator(r'^[a-zA-Z]{3}[0-9]{3}$', 'Wrong format. Please use ABC123 format.')
    license_number_format = RegexValidator(r'^[a-zA-Z0-9]{3,}$', 'Wrong format. Please use ABC123 format.')

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='plates', blank=False, null=False)
    license_number = models.CharField(max_length=10, unique=True, blank=False, null=False,
                                      validators=[license_number_format])
    detector = models.CharField(default="", max_length=50)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.license_number
