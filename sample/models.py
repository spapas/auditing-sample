from django.core.urlresolvers import reverse
from django.db import models

from auditable.models import Auditable
from simple_history.models import HistoricalRecords
import reversion

class Book(Auditable):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse("book_list")


class SHBook(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)

    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse("shbook_list")


@reversion.register
class RBook(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse("rbook_list")
        
    def get_versions(self):
        return reversion.get_for_object(self)
