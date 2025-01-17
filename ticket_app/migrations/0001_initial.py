# Generated by Django 5.1.1 on 2024-11-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('seat_number', models.CharField(max_length=10)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes/')),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
    ]
