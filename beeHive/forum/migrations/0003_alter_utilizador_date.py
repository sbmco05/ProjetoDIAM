# Generated by Django 4.2 on 2023-05-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_data_nascimento_utilizador_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
