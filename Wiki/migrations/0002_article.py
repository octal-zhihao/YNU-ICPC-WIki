# Generated by Django 3.2.8 on 2023-12-19 18:05

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('content', mdeditor.fields.MDTextField(blank=True, default='')),
                ('article_picture', models.ImageField(upload_to='img/', verbose_name='封面图')),
            ],
        ),
    ]