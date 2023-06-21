# Python
from datetime import datetime

# Django
from django.db import models
from django.db.models.query import QuerySet


class AbstractTrackingQuerySet(models.QuerySet):
    """AbstractTrackingQuerySet."""

    def delete(self) -> None:
        self.update(
            dt_deleted=datetime.now()
        )


class AbstractTrackingManager(models.Manager):
    """AbstractTrackingManager."""

    def get_queryset(self) -> QuerySet['AbstractTrackingModel']:
        return AbstractTrackingQuerySet(
            self.model,
            using=self._db
        )


class AbstractTrackingModel(models.Model):
    """AbstractTrackingModel."""

    dt_created: datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='datetime created'
    )
    dt_updated: datetime = models.DateTimeField(
        auto_now=True,
        verbose_name='datetime updated'
    )
    dt_deleted: datetime = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='datetime deleted'
    )
    objects = AbstractTrackingManager()

    def delete(self) -> None:
        self.dt_deleted = datetime.now()
        self.save(
            update_fields=('dt_deleted',)
        )

    class Meta:
        abstract = True


class AbstractConfig(AbstractTrackingModel):
    """AbstractConfig."""

    name: str = models.CharField(
        max_length=50,
        default='',
        verbose_name='name'
    )

    class Meta:
        abstract = True
