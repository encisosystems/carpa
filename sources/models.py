from django.contrib.gis.db import models as gis_models
from django.db import models
from main.models import BaseModel


class ParcelOwner(BaseModel):
    """

    """
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    organization = models.CharField(max_length=64, blank=True)
    address_1 = models.CharField(max_length=64, blank=True)
    address_2 = models.CharField(max_length=64, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    website = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = 'Parcel Owner'
        verbose_name_plural = 'Parcel Owners'

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'Owner-{self.pk}'


class Parcel(BaseModel):
    """

    """
    name = models.CharField(max_length=128, blank=True)
    owner = models.ForeignKey(ParcelOwner, on_delete=models.CASCADE)
    extension = models.DecimalField(max_digits=4, decimal_places=2, help_text='In hectares', null=True, blank=True)
    location = gis_models.PolygonField(
        help_text='Select at least 3 points to delimit a region. When you have finished, press click twice.',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Parcel'
        verbose_name_plural = 'Parcels'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'{self.owner}-parcel-{self.pk}'


class Driver(BaseModel):
    """

    """

    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=64, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    web = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
    
    def __str__(self):
        return self.name

class Vehicle(BaseModel, models.Model):
    """
    """

    plate = models.CharField(max_length=8, blank=True)
    model = models.CharField(max_length=64, blank=True)
    brand = models.CharField(max_length=20, blank=True)
    details = models.CharField(max_length=128, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank = True)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.enrollment

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

