# Generated by Django 2.0.7 on 2018-08-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20180730_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, default=None, help_text='Veuillez indiquer la quantité de lait bu par bébé', null=True, verbose_name='Quantité'),
        ),
    ]
