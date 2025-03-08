from django.db import models

class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} - {self.capacity} seats"
