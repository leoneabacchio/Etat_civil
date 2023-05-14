# Generated by Django 4.1.4 on 2023-01-25 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etatSevApp', '0044_delete_engeristrement'),
    ]

    operations = [
        migrations.CreateModel(
            name='engeristrement',
            fields=[
                ('NumE', models.AutoField(primary_key=True, serialize=False)),
                ('cle', models.IntegerField()),
                ('Date_E', models.DateField()),
                ('Heure_E', models.TimeField()),
                ('NumOff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etatSevApp.officier')),
                ('NumRegistre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etatSevApp.registre')),
            ],
        ),
    ]