# Generated by Django 4.2.4 on 2023-10-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_computer_update_date_alter_computer_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='os',
            field=models.ManyToManyField(to='Inventory.os_choice'),
        ),
    ]
