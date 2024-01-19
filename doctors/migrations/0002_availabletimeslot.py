# Generated by Django 4.2.6 on 2023-12-23 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
            ],
        ),
    ]