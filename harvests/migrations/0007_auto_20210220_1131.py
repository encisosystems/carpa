# Generated by Django 3.1.1 on 2021-02-20 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvests', '0006_auto_20210220_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunchbatch',
            name='bunch',
            field=models.ForeignKey(help_text='Aqui va la informacion del manojo', on_delete=django.db.models.deletion.CASCADE, to='harvests.bunch'),
        ),
    ]
