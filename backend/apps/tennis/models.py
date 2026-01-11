from django.db import models

# Create your models here.

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

class Tournament(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    association = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    surface = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    season = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ("external_id", "start_date")
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.name} {self.start_date.year}"
    
class TournamentResult(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="results"
    )
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        related_name="results"
    )
    round = models.CharField(max_length=50)
    points_earned = models.IntegerField()

    class Meta:
        ordering = ["tournament__start_date"]

    def __str__(self):
        return f"{self.player} - {self.tournament} ({self.round})"
    
class Ranking(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="rankings"
    )
    rank = models.IntegerField()
    points = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ("player", "date")
        ordering = ["rank"]

    def __str__(self):
        return f"{self.player} #{self.rank} ({self.date})"
