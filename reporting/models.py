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
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    #
    location = models.CharField(max_length=200)

    #
    incident_date = models.DateField()

    #
    additional_incident_data_infor = models.CharField(max_length=200)

    #
    source_date = models.DateField()

    #
    report_url = models.URLField(max_length=300)

    #
    source = models.CharField(max_length=200)

    incident_type = models.ForeignKey(IncidentType,
                                      on_delete=models.SET_NULL,
                                      null=True)

    #
    related_reports = models.ForeignKey('self', on_delete=models.CASCADE)

    #
    report_code = models.CharField(max_length=20)

    #
    weapon = models.ForeignKey(Weapon,
                               on_delete=models.SET_NULL,
                               null=True)

    #
    created_date = models.DateTimeField(
            default=timezone.now)

    #
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.report_code

