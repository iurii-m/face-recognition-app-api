from django.db import models
from django.contrib.postgres.fields import ArrayField


class Person(models.Model):
    name = models.CharField(max_length=100)
    embeddings = ArrayField(
            models.FloatField(),
            size=512,
        )

    def __str__(self):
        return self.name
