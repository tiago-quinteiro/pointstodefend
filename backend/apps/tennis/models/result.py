class Result(models.Model):
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