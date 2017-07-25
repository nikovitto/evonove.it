from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.models import Image
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class AgencyPage(Page):
    pass


class TeamMember(Orderable):
    page = ParentalKey(AgencyPage, related_name='team')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='team_profile')

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=150, help_text=_('Team member company role'))
    bio = RichTextField(max_length=360, help_text=_('The team member bio'))
    gravatar = models.CharField(max_length=150, help_text=_('Add your Gravatar email'), null=True, blank=True)
    photo = models.ForeignKey(Image, null=True, blank=True, related_name='+')

    website = models.URLField(help_text=_('Your website page URL'), null=True, blank=True)
    github = models.URLField(help_text=_('Your GitHub page URL'), null=True, blank=True)
    stackoverflow = models.URLField(help_text=_('Your Stack Overflow page URL'), null=True, blank=True)
    twitter = models.URLField(help_text=_('Your Twitter page URL'), null=True, blank=True)
    gplus = models.URLField(help_text=_('Your Google+ page URL'), null=True, blank=True)
    facebook = models.URLField(help_text=_('Your Facebook page URL'), null=True, blank=True)
    linkedin = models.URLField(help_text=_('Your LinkedIn page URL'), null=True, blank=True)

    medium = models.URLField(help_text=_('Your Medium page URL'), null=True, blank=True)
    behance = models.URLField(help_text=_('Your Behance page URL'), null=True, blank=True)
    dribbble = models.URLField(help_text=_('Your Dribble page URL'), null=True, blank=True)
    flickr = models.URLField(help_text=_('Your Flickr page URL'), null=True, blank=True)
    tumblr = models.URLField(help_text=_('Your Tumblr page URL'), null=True, blank=True)
    deviantart = models.URLField(help_text=_('Your DeviantArt page URL'), null=True, blank=True)
    pinterest = models.URLField(help_text=_('Your Pinterest page URL'), null=True, blank=True)

    @property
    def full_name(self):
        return '{} {}'.format(self.firstname, self.lastname)

    panels = [
        FieldPanel('user'),

        FieldPanel('firstname'),
        FieldPanel('lastname'),
        FieldPanel('role'),
        FieldPanel('bio'),
        FieldPanel('gravatar'),
        ImageChooserPanel('photo'),

        FieldPanel('website'),
        FieldPanel('github'),
        FieldPanel('stackoverflow'),
        FieldPanel('twitter'),
        FieldPanel('gplus'),
        FieldPanel('facebook'),
        FieldPanel('linkedin'),

        FieldPanel('medium'),
        FieldPanel('behance'),
        FieldPanel('dribbble'),
        FieldPanel('flickr'),
        FieldPanel('tumblr'),
        FieldPanel('deviantart'),
        FieldPanel('pinterest'),
    ]
