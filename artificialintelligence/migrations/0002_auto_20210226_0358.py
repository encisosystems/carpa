# Generated by Django 3.1.1 on 2021-02-26 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvests', '0010_auto_20210226_0358'),
        ('artificialintelligence', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processedimage',
            name='bunches',
        ),
        migrations.AddField(
            model_name='processedimage',
            name='bunch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='harvests.bunch'),
        ),
        migrations.AlterField(
            model_name='processedimage',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='processedimage',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Last modified'),
        ),
    ]
