# Generated by Django 4.0.1 on 2022-01-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.CharField(max_length=250, verbose_name='api')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('auth', models.CharField(max_length=250, verbose_name='Auth')),
                ('https', models.BooleanField(verbose_name='https')),
                ('cors', models.CharField(max_length=250, verbose_name='Cors')),
                ('link', models.CharField(max_length=250, verbose_name='Link')),
                ('category', models.CharField(max_length=250, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Entry',
            },
        ),
    ]
