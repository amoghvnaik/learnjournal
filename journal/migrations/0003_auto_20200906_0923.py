# Generated by Django 3.1.1 on 2020-09-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20200905_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('software', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Resources',
        ),
    ]
