# Generated by Django 4.2.5 on 2023-09-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardcomp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="annual_fees_remark",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="card",
            name="joining_fees_remark",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
