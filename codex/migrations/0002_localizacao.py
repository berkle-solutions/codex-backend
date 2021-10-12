# Generated by Django 3.2.8 on 2021-10-12 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloco', models.CharField(max_length=45)),
                ('andar', models.CharField(max_length=45)),
                ('unidade', models.CharField(max_length=45)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codex.pessoa')),
            ],
        ),
    ]