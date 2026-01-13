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