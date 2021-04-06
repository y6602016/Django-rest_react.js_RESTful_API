# Generated by Django 3.1.7 on 2021-04-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210406_0453'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]