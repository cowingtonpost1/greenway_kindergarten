from django.db import models
from django.utils import timezone

CATEGORIES = (
    ("R", "Reading"),
    ('M', 'Math'),
    ("W", "Writing"),
    ("P", "Phonics"),
    ("S", "Science/Social Studies"),
    ("SEL", "Social Emotional Learning"),
)


class Project(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    video = models.CharField(max_length=250, default='')
    date_posted = models.DateTimeField(timezone.now)
    category = models.CharField(max_length=3, choices=CATEGORIES)
