# Generated by Django 4.2.17 on 2025-01-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_contacts_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='reservation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
