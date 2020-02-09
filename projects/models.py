from django.db import models


class Projects(models.Model):
    name = models.CharField(unique=True, max_length=120)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
