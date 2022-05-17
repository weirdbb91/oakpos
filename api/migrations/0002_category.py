# Generated by Django 4.0.3 on 2022-05-17 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('description', models.TextField(blank=True, null=True, verbose_name='설명')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category', verbose_name='상위 카테고리')),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리 리스트',
                'ordering': ['id'],
            },
        ),
    ]