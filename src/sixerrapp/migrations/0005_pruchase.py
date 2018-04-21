# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 03:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sixerrapp', '0004_profile_slogan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pruchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sixerrapp.Gig')),
            ],
        ),
    ]
