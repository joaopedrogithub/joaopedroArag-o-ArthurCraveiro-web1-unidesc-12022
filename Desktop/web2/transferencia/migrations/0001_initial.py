# Generated by Django 4.0.4 on 2022-06-22 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=100)),
                ('cod_identificacao', models.CharField(max_length=100)),
            ],
        ),
    ]
