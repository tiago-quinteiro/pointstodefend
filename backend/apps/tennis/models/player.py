from django.db import models

class Player(models.Model):
    external_id = models.CharField(
        max_length=100,
        unique=True,
        help_text="ID from external tennis data source"
    )
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=3)
    picture_path = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name