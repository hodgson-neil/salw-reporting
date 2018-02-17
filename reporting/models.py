from django.db import models

from django.utils import timezone


class Report(models.Model):

    SOUTH_AMERICA = 'SAM'
    CENTRAL_AMERICA = 'CAM'
    EAST_ASIA_PAC = 'EAPAC'
    NORTH_AFRICA = 'NAFR'
    WEST_AFRICA = 'WAFR'
    CENTRAL_AFRICA = 'CAFR'
    EAST_AFRICA = 'EAFR'
    REGION_CHOICES = (
        (SOUTH_AMERICA, 'South America'),
        (CENTRAL_AMERICA, 'Central America'),
        (EAST_ASIA_PAC, 'East Asia / Pacific'),
        (NORTH_AFRICA, 'North Africa'),
        (WEST_AFRICA, 'West Africa'),
        (CENTRAL_AFRICA, 'Central Africa'),
        (EAST_AFRICA, 'East Africa'),
    )

    PISTOL = 'PISTOL'
    REVOLVER = 'REVOLVER'
    RIFEL = 'RIFEL'
    SHOTGUN = 'SHOTGUN'
    SMALL_ARMS_AMMUNITION = 'SMALL_ARMS_AMMUNITION' 
    MACHINE_GUN = 'MACHINE_GUN'
    EXPLOSIVE_ORDNANCE = 'EXPLOSIVE_ORDNANCE'
    ATGM = 'ATGM'
    MANPADS = 'MANPADS'
    UNSPECIFIED = 'UNSPECIFIED'
    OTHER = 'OTHER'
    
    WEAPONS_CHOICES = (
        (PISTOL, 'Pistol'),
        (REVOLVER, 'Revolver'),
        (RIFEL, 'Rifel'),
        (SHOTGUN, 'Shotgun'),
        (SMALL_ARMS_AMMUNITION, 'Small Arms Ammunition'),
        (MACHINE_GUN, 'Machine Gun'),
        (EXPLOSIVE_ORDNANCE, 'Explosive Ordnance'),
        (ATGM, 'ATGM'),
        (MANPADS, 'MANPADS'),
        (UNSPECIFIED, 'Unspecified'),
        (OTHER, 'Other'),
    )

    LOSS = 'LOSS'
    LOOTING = 'LOOT'
    UNAUTH_TRANSFER_OR_USE = 'UNTRU'
    CORRUPT_SALE_OR_RENT = 'CSR'
    SEIZURE = 'SEIZ'
    DIVERTED = 'DIV'
    LAW = 'LAW'
    DESERTION = 'DESERT'
    UNPLANNED = 'UNPLANNED'
    SAFETY_SECURITY = 'SAFSEC'
    DISARMAMENT = 'DISARM'
    AMNESTY = 'AM'

    INCIDENT_CHOICES = (
        (LOSS, 'Loss'),
        (LOOTING, 'Looting'),
        (UNAUTH_TRANSFER_OR_USE, 'Unauthorized transfer or use'),
        (CORRUPT_SALE_OR_RENT, 'Corrupt sale or rent'),
        (SEIZURE, 'Seizure'),
        (DIVERTED, 'Use of diverted weapons(in criminal, terrorist or insurgency incidents)'),
        (LAW, 'Law enforcement(law enforcement action, court cases, investigation, government campaigns & action)'),
        (DESERTION, 'Desertion with weapons'),
        (UNPLANNED, 'Unplanned explosions at munitions sites(UEMS)'),
        (SAFETY_SECURITY, 'Safety and security'),
        (DISARMAMENT, 'Disarmament'),
        (AMNESTY, 'Weapons amnesty'),
        (OTHER, 'Other')
    )

    #
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    #
    headline = models.CharField(max_length=200)

    #
    summary = models.TextField()

    #
    region = models.CharField(
        max_length=20,
        choices=REGION_CHOICES,
    )

    #
    country = models.CharField(max_length=3)

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

    incident_type = models.CharField(
        max_length=20,
        choices=INCIDENT_CHOICES,
    )

    #
    related_reports = models.ForeignKey('self', on_delete=models.CASCADE)

    #
    report_code = models.CharField(max_length=20)

    #
    weapons = models.CharField(
        max_length=20,
        choices=WEAPONS_CHOICES,
    )

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

