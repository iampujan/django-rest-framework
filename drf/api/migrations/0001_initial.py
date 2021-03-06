# Generated by Django 2.1.7 on 2019-04-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('seller_email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('expire_at', models.DateField()),
                ('discount_precent', models.FloatField()),
            ],
        ),
    ]
