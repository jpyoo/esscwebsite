# Generated by Django 4.2.2 on 2024-01-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_archivebanners'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArchiveBanners',
        ),
        migrations.AddField(
            model_name='member',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='pronouns',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]