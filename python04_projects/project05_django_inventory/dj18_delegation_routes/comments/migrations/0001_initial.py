# Generated by Django 5.0.1 on 2024-02-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=3)),
                ('commet', models.TextField(max_length=1000, null=True)),
                ('date', models.DateField(null=True)),
                ('signature', models.CharField(default='Firma', max_length=100)),
            ],
        ),
    ]