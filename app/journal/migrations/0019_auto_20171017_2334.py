# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("journal", "0018_interest")]

    operations = [migrations.RenameModel(old_name="Interest", new_name="Tag")]
