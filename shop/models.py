from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class Product(models.Model):
    class Statuses(models.TextChoices):
        IN_STOCK = "in_stock", _("In stock")
        UNDER_ORDER = "under_order", _("Under the order")
        ADMISSION = "admisson", _("Expecting admission")
        NOT_IN_STOCK = "not_in_stock", _("Not in the stock")
        NOT_MANUFACTURING = "not_manufacturing", _("Not manifacturing")

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.CharField(
        max_length=20, choices=Statuses.choices, default=Statuses.IN_STOCK
    )
    image = ResizedImageField(force_format="WEBP", quality=75, upload_to="images/")

    def __str__(self):
        return f"#{self.id} {self.name}"
