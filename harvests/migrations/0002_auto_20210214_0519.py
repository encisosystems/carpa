# Generated by Django 3.1.1 on 2021-02-14 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunch',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvests.categorybunch'),
        ),
    ]
