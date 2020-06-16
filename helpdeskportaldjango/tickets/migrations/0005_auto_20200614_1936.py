# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-06-14 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import tickets.enums


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_imagefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('CONNECTIVITY', 'Connectivity'), ('MEDICAL', 'Medical'), ('PLUMBING', 'Plumbing'), ('STRUCTURAL', 'Structural'), ('ELECTRICAL', 'Electrical'), ('OTHER', 'Other')], default=tickets.enums.Category('Other'), max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='location',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('HOSTEL', 'Hostel'), ('HOSTELROOM', 'Hostel Room'), ('LIBRARY', 'Library'), ('LECTUREHALL1', 'Lecture Hall 1'), ('LECTUREHALL2', 'Lecture Hall 2'), ('PLAYGROUND', 'Playground'), ('OTHER', 'Other')], default=tickets.enums.Location('Admin'), max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='unit_number',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
