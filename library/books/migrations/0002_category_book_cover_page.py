# Generated by Django 4.1.13 on 2024-09-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_cat', models.ImageField(default='', upload_to='upload/book/')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cover_page',
            field=models.ImageField(default='', upload_to='upload/book/'),
        ),
    ]
