from django.db import models

from django.utils import timezone


class Region(models.Model):
    name = models.CharField(max_length=25)


class Country(models.Model):
    name = models.CharField(max_length=25)
    iso_country_code = models.CharField(max_length=3)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)


class Weapon(models.Model):
    type = models.CharField(max_length=30)


class IncidentType(models.Model):
    description = models.CharField(max_length=200)


class Report(models.Model):

    #
    author = models.ForeignKey('auth.User',
                               on_delete=models.SET_NULL,
                               null=True)

    #
    headline = models.CharField(max_length=200)

    #
    summary = models.TextField()

    #
    country = models.ForeignKey(Country,
                                on_delete=models.SET_NULL,
                                null=True, blank=True)

    #
    location = models.CharField(max_length=200)

    #
    incident_date = models.DateField()

    #
    additional_incident_data_info = models.CharField(max_length=200,
                                                     null=True, blank=True)

    #
    source_date = models.DateField()

    #
    report_url = models.URLField(max_length=300, null=True, blank=True)

    #
    source = models.CharField(max_length=200, null=True, blank=True)

    incident_types = models.ManyToManyField(IncidentType)

    #
    related_reports = models.ManyToManyField('self')

    #
    report_code = models.CharField(max_length=20)

    #
    weapons = models.ManyToManyField(Weapon)

    #
    created_date = models.DateTimeField(
            default=timezone.now)

    #
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.report_code

