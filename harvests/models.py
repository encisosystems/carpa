
from django.db import models
# from django.db.models.signals import post_save
from main.models import BaseModel


class CategoryBunch(BaseModel, models.Model):
    """

    """

    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'BunchCategory'
        verbose_name_plural = 'BunchCategories'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'Category-{self.pk}'


# def show_location(sender, instance, **kwargs):
#     print(f'My coordinates: {instance.location}')
#
# post_save.connect(show_location, sender=BatchSource)


class Bunch(BaseModel, models.Model):
    """

    """

    category = models.ForeignKey(CategoryBunch, on_delete=models.CASCADE, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Bunch'
        verbose_name_plural = 'Bunches'

    def __str__(self):
        return f'Bunch-{self.pk}'
