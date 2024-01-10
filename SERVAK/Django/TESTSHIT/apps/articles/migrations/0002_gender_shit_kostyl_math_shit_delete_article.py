# Generated by Django 4.2.6 on 2023-12-24 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender_shit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('1', 'parquet'), ('2', 'laminate'), ('3', 'helicopter boss')], max_length=20, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Kostyl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.gender_shit')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Math_shit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math', models.CharField(choices=[('1', 'Gamma function'), ('2', 'Series of inverse squares'), ('3', 'Gaussian integral')], max_length=20, verbose_name='Fav_obj')),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
