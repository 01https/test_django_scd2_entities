import hashlib
import uuid

from django.db import models
from django.utils import timezone

class EntityType(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Entity(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=255)
    type = models.ForeignKey("EntityType", on_delete=models.PROTECT)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField(null=True, blank=True)
    is_current = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["uid", "is_current"])
        ]

    def __str__(self):
        return self.display_name


class EntityDetail(models.Model):
    entity = models.ForeignKey("Entity", on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    value = models.TextField()
    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField(null=True, blank=True)
    is_current = models.BooleanField(default=True)
    hash_diff = models.CharField(max_length=64, editable=False)

    class Meta:
        indexes = [
            models.Index(fields=["entity", "code", "is_current"])
        ]

    def save(self, *args, **kwargs):
        self.hash_diff = hashlib.sha256(str(self.value).encode()).hexdigest()
        super().save(*args, **kwargs)
