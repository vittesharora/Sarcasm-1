# Generated by Django 2.0.13 on 2019-08-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190808_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='audiofile',
            field=models.FileField(blank=True, null=True, upload_to='static/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='level',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='static/', verbose_name=''),
        ),
    ]