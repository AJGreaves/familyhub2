# Generated by Django 3.0.4 on 2020-04-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approved',
            field=models.CharField(choices=[('Awaiting reply', 'Awaiting reply'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Awaiting reply', max_length=20),
        ),
    ]