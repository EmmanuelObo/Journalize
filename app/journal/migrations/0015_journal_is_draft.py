# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("journal", "0014_remove_journal_is_draft")]

    operations = [
        migrations.AddField(
            model_name="journal",
            name="is_draft",
            field=models.BooleanField(default=False),
        )
    ]
