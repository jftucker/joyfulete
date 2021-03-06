# Generated by Django 3.0.5 on 2020-04-24 03:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeekType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('numStrength', models.IntegerField(blank=True, null=True)),
                ('numActiveRecovery', models.IntegerField(blank=True, null=True)),
                ('numRecovery', models.IntegerField(blank=True, null=True)),
                ('numAerobicBase', models.IntegerField(blank=True, null=True)),
                ('numMuscularEndurance', models.IntegerField(blank=True, null=True)),
                ('numHighIntensity', models.IntegerField(blank=True, null=True)),
                ('percentDistanceStrength', models.FloatField(blank=True, null=True)),
                ('percentDistanceActiveRecovery', models.FloatField(blank=True, null=True)),
                ('percentDistanceRecovery', models.FloatField(blank=True, null=True)),
                ('percentDistanceAerobicBase', models.FloatField(blank=True, null=True)),
                ('percentDistanceMuscularEndurance', models.FloatField(blank=True, null=True)),
                ('percentDistanceHighIntensity', models.FloatField(blank=True, null=True)),
                ('percentVerticalStrength', models.FloatField(blank=True, null=True)),
                ('percentVerticalActiveRecovery', models.FloatField(blank=True, null=True)),
                ('percentVerticalRecovery', models.FloatField(blank=True, null=True)),
                ('percentVerticalAerobicBase', models.FloatField(blank=True, null=True)),
                ('percentVerticalMuscularEndurance', models.FloatField(blank=True, null=True)),
                ('percentVerticalHighIntensity', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('gain', models.IntegerField(blank=True, null=True)),
                ('days', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='weeks', to='plans.Day')),
                ('weekType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='weeks', to='plans.WeekType')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weeks', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plans', to='plans.Week')),
            ],
        ),
        migrations.CreateModel(
            name='MacroPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('athleteCategory', models.IntegerField(choices=[(1, 'Category 1'), (2, 'Category 2')], default=1)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('weekFramework', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='macro_plans', to='plans.WeekType')),
            ],
        ),
    ]
