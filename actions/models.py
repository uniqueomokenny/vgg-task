from django.db import models

from projects.models import Projects


class Actions(models.Model):
    project_id = models.ForeignKey(
        Projects, on_delete=models.CASCADE, related_name='actions')
    description = models.CharField(max_length=255)
    note = models.CharField(max_length=255)

    def __str__(self):
        return self.project_id.name
