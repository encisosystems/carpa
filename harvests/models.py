from django.contrib.gis.db import models as gis_models
from django.db import models
# from django.db.models.signals import post_save
from main.models import BaseModel


class CategoryBunch(BaseModel, models.Model):
    """

    """

    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'BunchCategory'
        verbose_name_plural = 'BunchCategories'

    def __str__(self):
        return self.name


class BatchSource(BaseModel, models.Model):
    """

    """

    location = gis_models.PolygonField(
        help_text='Select at least 3 points to delimit a region. When finished, press click twice.',
        null=True,
        blank=True
    )
    city = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = 'BatchSource'
        verbose_name_plural = 'BatchSources'

    def __str__(self):
        return self.city


# def show_location(sender, instance, **kwargs):
#     print(f'My coordinates: {instance.location}')
#
# post_save.connect(show_location, sender=BatchSource)


class Bunch(BaseModel, models.Model):
    """

    """

    category = models.ForeignKey(CategoryBunch, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Bunch'
        verbose_name_plural = 'Bunches'

    def __str__(self):
        return f'Bunch-{self.pk}'


class BunchBatch(BaseModel, models.Model):
    bunch = models.ForeignKey(Bunch, on_delete=models.CASCADE)
    batch_source = models.ForeignKey(BatchSource, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bunch Batch'
        verbose_name_plural = 'Bunches Batch'

    def __str__(self):
        return f'Bunch Batch-{self.pk}'



