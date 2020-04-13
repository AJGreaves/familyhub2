# Generated by Django 3.0.4 on 2020-04-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200413_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Awaiting response', 'Awaiting response'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Awaiting response', max_length=20),
        ),
    ]
