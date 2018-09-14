# Generated by Django 2.0.7 on 2018-08-20 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180818_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='artist',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='type',
        ),
        migrations.AddField(
            model_name='question',
            name='branch',
            field=models.CharField(choices=[('CSE', 'cse'), ('ECE', 'ece'), ('EEE', 'eee'), ('IT', 'it')], default=0.1388888888888889, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=32),
        ),
    ]
