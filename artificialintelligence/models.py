from django.db import models
from harvests.models import Bunch
from main.models import BaseModel


class ProcessedImage(BaseModel):
    """

    """
    label = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='AI/images/', null=True, blank=True)
    bunch = models.ForeignKey(Bunch, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Processed Image'
        verbose_name_plural = 'Processed Images'

    def __str__(self):
        if self.label:
            return self.label
        return f'Processed-Image-{self.pk}'
