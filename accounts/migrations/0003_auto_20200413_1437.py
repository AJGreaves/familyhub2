# Generated by Django 3.0.4 on 2020-04-13 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_application_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='approved',
            new_name='status',
        ),
    ]