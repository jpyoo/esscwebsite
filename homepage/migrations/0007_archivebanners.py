# Generated by Django 4.2.2 on 2024-01-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_rename_social1_member_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveBanners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/Home2/')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]