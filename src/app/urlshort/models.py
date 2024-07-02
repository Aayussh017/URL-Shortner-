from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone

class ShortURL(models.Model):
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100, unique=True)
    time_date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_unique_short_url()
        super().save(*args, **kwargs)

    def generate_unique_short_url(self):
        while True:
            short_url = get_random_string(length=8)
            if not ShortURL.objects.filter(short_url=short_url).exists():
                break
        return short_url

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"