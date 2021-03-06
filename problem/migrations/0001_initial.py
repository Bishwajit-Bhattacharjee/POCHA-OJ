# Generated by Django 2.2.10 on 2020-06-14 16:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import problem.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('statement', models.FileField(upload_to='problem_statements/%Y/%m/%d')),
                ('time_limit', models.FloatField(default=3.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('memory_limit', models.PositiveSmallIntegerField(default=256, validators=[django.core.validators.MaxValueValidator(1024)])),
                ('is_public', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('judge_solution', models.FileField(blank=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_problems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_file', models.FileField(blank=True, upload_to=problem.models.get_testcase_path)),
                ('is_sample', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcases', to='problem.Problem')),
            ],
        ),
    ]
