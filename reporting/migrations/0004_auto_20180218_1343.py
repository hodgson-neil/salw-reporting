# Generated by Django 2.0.2 on 2018-02-18 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0003_auto_20180218_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='incident_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reporting.IncidentType'),
        ),
        migrations.AlterField(
            model_name='report',
            name='related_reports',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reporting.Report'),
        ),
    ]
