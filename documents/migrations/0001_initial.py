# Generated by Django 3.2.3 on 2021-11-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='myFiles')),
                ('nom', models.CharField(max_length=50)),
                ('typeFile', models.CharField(max_length=50)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
