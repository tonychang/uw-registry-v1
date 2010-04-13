from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service (models.Model):

    #constants
    SUBMIT_STAT     = 1
    DENY_STAT       = 2
    APPROVE_STAT    = 3

    STATUS_CHOICES = (
            (SUBMIT_STAT, 'Submitted'),
            (DENY_STAT, 'Denied'),
            (APPROVE_STAT, 'Approved'),
            )

    #fields
    name = models.CharField(
            max_length=255, 
            unique=True, 
            help_text="Type in the full name of your service",
            )

    nickname = models.SlugField(
            unique=True, 
            max_length=100, 
            help_text="Choose a shortname for your service",
            )

    description = models.TextField(
            max_length=10000, 
            help_text="Type in a description for your service so people know what it does",
            )
    
    notes = models.TextField(
            max_length=10000, 
            help_text="Area to place extra notes on this service such as why does this service git approved or denied",
            )

    owner = models.ForeignKey(User,) 

    support_contact = models.EmailField(
            help_text="Email address of the service owner",
            )

    doc_url = models.URLField(
            help_text="Type in the url to your service documentation",
            )

    root_url = models.URLField(
            help_text="Type in the service url that you want exposed to applications",
			verify_exists=False,
            )

    status = models.IntegerField(
            choices=STATUS_CHOICES, 
            help_text="Choose from: submitted, denied, approved",
            )

    date_submitted = models.DateTimeField()

    date_modified = models.DateTimeField()

    #methods
    def __unicode__ (self):
        return self.nickname;

    def get_absolute_url(self):
        return "/%s/" % self.nickname;
