# Generated by Django 2.2 on 2020-05-05 17:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


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
                ('statement', models.TextField()),
                ('time_limit', models.FloatField(default=3.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('memory_limit', models.PositiveSmallIntegerField(default=256, validators=[django.core.validators.MaxValueValidator(1024)])),
                ('is_public', models.BooleanField(default=False)),
                ('adding_time', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_problems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_input', models.TextField()),
                ('expected_output', models.TextField()),
                ('is_sample', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcases', to='problem.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('code', models.TextField()),
                ('time_required', models.FloatField(blank=True, null=True)),
                ('memory_required', models.IntegerField(blank=True, null=True)),
                ('language', models.SmallIntegerField(choices=[(1, 'C'), (2, 'CPP'), (3, 'JAVA'), (4, 'PYTHON')], default=2)),
                ('verdict', models.SmallIntegerField(choices=[(1, 'WRONG ANSWER'), (2, 'ACCEPTED'), (3, 'TLE'), (4, 'MLE'), (7, 'RUNTIME ERROR'), (5, 'RUNNING'), (6, 'IN QUEUE')], default=6)),
                ('on_test_case', models.SmallIntegerField(default=0)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='problem.Problem')),
            ],
        ),
    ]
