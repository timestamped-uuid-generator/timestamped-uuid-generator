from django.utils import timezone
from django.db import models
import uuid as uuid_lib


class TimeStampedUUID(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    uuid = models.UUIDField(unique=True, default=uuid_lib.uuid4)

