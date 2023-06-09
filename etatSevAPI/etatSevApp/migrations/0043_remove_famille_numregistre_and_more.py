# Generated by Django 4.1.4 on 2023-01-25 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etatSevApp', '0042_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='famille',
            name='NumRegistre',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='NumRegistre',
        ),
        migrations.RemoveField(
            model_name='personnedeces',
            name='NumRegistre',
        ),
        migrations.CreateModel(
            name='engeristrement',
            fields=[
                ('NumE', models.AutoField(primary_key=True, serialize=False)),
                ('cle', models.IntegerField()),
                ('NumOff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etatSevApp.officier')),
                ('NumRegistre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etatSevApp.registre')),
            ],
        ),
    ]
