# Generated by Django 3.2.8 on 2021-10-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0002_localizacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusFila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
    ]