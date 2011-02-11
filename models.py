from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserVoiceId( models.Model ):
    service     = models.ForeignKey('Service',)
    category_id = models.IntegerField()
    class Meta:
        unique_together = ("service", "category_id")

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
            null=True,
            help_text="Area to place extra notes related to this service",
            )

    owner = models.ForeignKey(User,) 

    support_contact = models.EmailField(
            help_text="Email address of the service owner",
            )

    doc_url = models.URLField(
            help_text="Type in the url to your service documentation",
			verify_exists=False,
			null=True,
                        blank=True
            )

    root_url = models.URLField(
            help_text="Type in the service url that you want exposed to applications",
			verify_exists=False,
			null=True,
                        blank=True
        
            )

    root_url_hidden = models.BooleanField(
            help_text="Check this if you want your web services hidden to the public",
			blank=True,
            )

    status = models.IntegerField(
            choices=STATUS_CHOICES, 
            help_text="Choose from: submitted, denied, approved",
            )

    date_submitted = models.DateTimeField()

    date_modified = models.DateTimeField()

    in_development = models.BooleanField(
			default=False,
			help_text="Check this if your service is in development. Production requires both doc and root urls.")

    user_voice_categories = models.ManyToManyField(UserVoiceId, verbose_name="list of UserVoice categories", related_name="%(app_label)s_%(class)s_related")

    #methods
    def __unicode__ (self):
        return self.nickname;

    def get_absolute_url(self):
        return "/%s/" % self.nickname;

