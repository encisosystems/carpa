from django.db import models
# from django.db.models.signals import post_save
from main.models import BaseModel
from harvests.models import BunchBatch


class Report(BaseModel):
    """

    """

    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    block = models.CharField(max_length = 16, blank=True)
    lot = models.CharField(max_length = 16, blank=True)
    bunchBatch = models.ForeignKey(BunchBatch, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return f'Report-{self.bunchBatch.parcel.name}-{self.block}-{self.lot}'

