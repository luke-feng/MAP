# Generated by Django 3.1.6 on 2021-02-19 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('sectorid', models.AutoField(db_column='SectorID', primary_key=True, serialize=False)),
                ('sectorname', models.TextField(db_column='SectorName')),
                ('modifytime', models.TextField(blank=True, db_column='ModifyTime', null=True)),
            ],
        ),
    ]
