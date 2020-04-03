from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from web_site.fields import PublicFileField
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
    # video = models.CharField(max_length=250, default='')
    video = PublicFileField(_('file'))
    date_posted = models.DateTimeField(timezone.now)
    category = models.CharField(max_length=3, choices=CATEGORIES)
