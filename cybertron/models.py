from django.db import models

class CybersecurityEvent(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.event_type} - {self.timestamp}'
