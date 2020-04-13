# Generated by Django 3.0.4 on 2020-04-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200413_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Awaiting reply', 'Awaiting response'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Awaiting reply', max_length=20),
        ),
    ]
