# Generated by Django 3.0.7 on 2021-01-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210112_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yname', models.CharField(max_length=30)),
                ('yemail', models.CharField(max_length=30)),
                ('ysubject', models.CharField(max_length=30)),
                ('ymessage', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
