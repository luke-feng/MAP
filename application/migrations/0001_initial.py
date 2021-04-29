# Generated by Django 3.1.6 on 2021-03-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.AutoField(db_column='ApplicationID', primary_key=True, serialize=False)),
                ('fisrt_name', models.TextField(blank=True, db_column='FisrtName', null=True)),
                ('last_name', models.TextField(blank=True, db_column='LastName', null=True)),
                ('email_address', models.TextField(blank=True, db_column='EmailAddress', null=True)),
                ('password', models.TextField(blank=True, db_column='Password', null=True)),
                ('postal_code', models.IntegerField(blank=True, db_column='Postalcode', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('user_scale', models.TextField(blank=True, db_column='UserScale', null=True)),
                ('revenue', models.TextField(blank=True, db_column='Revenue', null=True)),
                ('modify_time', models.DateTimeField(auto_now=True, db_column='ModifyTime', null=True)),
                ('processed', models.BooleanField(blank=True, db_column='Processed', default=False, null=True)),
            ],
            options={
                'db_table': 'Application',
                'managed': False,
            },
        ),
    ]