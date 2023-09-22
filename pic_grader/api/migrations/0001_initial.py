# Generated by Django 4.2.5 on 2023-09-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=8, unique=True)),
                ('picture', models.ImageField(default='images/default.png', upload_to='images/')),
                ('rank', models.IntegerField(default=800, null=True)),
                ('plec', models.CharField(default='', max_length=2)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]