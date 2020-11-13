# Generated by Django 3.1.2 on 2020-11-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
