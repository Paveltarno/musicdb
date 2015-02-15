# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_auto_20150215_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name']},
        ),
    ]
