# Generated by Django 4.2.4 on 2023-10-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_rename_computers_computer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='added_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='pc_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
