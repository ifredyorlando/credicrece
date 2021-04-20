from django.db import models

from utils.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _
import datetime

class Caja(BaseModel):
    monto = models.FloatField(_('Monto de caja'),default=0.0)
    updated_at = models.DateTimeField(default=datetime.date.today)