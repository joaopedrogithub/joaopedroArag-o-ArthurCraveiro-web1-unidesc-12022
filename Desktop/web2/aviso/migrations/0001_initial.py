# Generated by Django 4.0.4 on 2022-06-22 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula_avi', models.CharField(max_length=100)),
                ('assunto_avi', models.CharField(max_length=100)),
                ('data_avi', models.CharField(max_length=100)),
            ],
        ),
    ]