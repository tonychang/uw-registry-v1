from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service (models.Model):

    SUBMIT_STAT     = 1
    DENY_STAT       = 2
    APPROVE_STAT    = 3

    STATUS_CHOICES = (
            (SUBMIT_STAT, 'Submitted'),
            (DENY_STAT, 'Denied'),
            (APPROVE_STAT, 'Approved'),
            )

    name            = models.CharField(max_length=255, unique=True)
    nickname        = models.SlugField(unique=True, max_length=100)
    description     = models.CharField(max_length=10000)
    owner           = models.ForeignKey(User)
    support_contact = models.EmailField()
    doc_url         = models.URLField()
    root_url        = models.URLField()
    status          = models.IntegerField(choices=STATUS_CHOICES)
    date_submitted  = models.DateTimeField()
    date_modified   = models.DateTimeField()

    def __unicode__ (self):
        return self.nickname;


