# Generated by Django 4.0.5 on 2022-08-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category_image', models.ImageField(upload_to='imgs/')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='imgs/')),
                ('detail', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='main.category')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
