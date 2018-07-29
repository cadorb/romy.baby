# Generated by Django 2.0.7 on 2018-07-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_auto_20180727_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('BOTTLE', 'Biberon'), ('BATH', 'Bain'), ('PEE', 'Pipi'), ('POOH', 'Popo'), ('SLEEP', 'Dodo')], help_text="Veuillez indiquer le type de l'activité", max_length=6),
        ),
    ]
