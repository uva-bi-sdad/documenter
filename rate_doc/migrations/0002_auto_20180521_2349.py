# Generated by Django 2.0.5 on 2018-05-21 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_doc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='isNew',
            field=models.BooleanField(default=False, verbose_name='Article Mentions New Product?'),
        ),
    ]
