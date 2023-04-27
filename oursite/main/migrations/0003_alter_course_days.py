# Generated by Django 4.0.7 on 2023-04-25 19:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_application_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'M'), ('T', 'T'), ('W', 'W'), ('TH', 'T'), ('F', 'F')], max_length=50),
        ),
    ]