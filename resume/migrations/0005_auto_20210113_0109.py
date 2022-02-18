# Generated by Django 3.0.7 on 2021-01-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20210112_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homelem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='images/')),
                ('Name', models.CharField(max_length=30)),
                ('About', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='resume',
            name='Linkedin',
            field=models.CharField(max_length=50),
        ),
    ]
