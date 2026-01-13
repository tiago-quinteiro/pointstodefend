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