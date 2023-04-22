# Generated by Django 4.1.7 on 2023-04-22 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(choices=[('SPRING', 'SPRING'), ('SUMMER', 'SUMMER'), ('FALL', 'FALL')], default='SPRING', max_length=6)),
                ('year', models.CharField(default='23', max_length=2)),
                ('current', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('closed', 'Closed'), ('open', 'Open')], max_length=6)),
                ('total_postitions', models.IntegerField(default=10)),
                ('total_filled', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='filled',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('pending', 'Pending'), ('hired', 'Hired')], default='available', max_length=10),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=40)),
                ('link', models.CharField(max_length=40)),
                ('current', models.BooleanField(default=True)),
                ('application_status', models.CharField(choices=[('offer sent', 'Offer Sent'), ('rejected', 'Rejected'), ('accepted offer', 'Accepted Offer')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
