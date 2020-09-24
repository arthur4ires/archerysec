# Generated by Django 2.1.8 on 2020-05-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0007_auto_20200503_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='dockle_scan_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_id', models.UUIDField(blank=True, null=True)),
                ('rescan_id', models.TextField(blank=True, null=True)),
                ('scan_date', models.TextField(blank=True, null=True)),
                ('project_id', models.UUIDField(blank=True, null=True)),
                ('project_name', models.TextField(blank=True, null=True)),
                ('total_vuln', models.IntegerField(blank=True, null=True)),
                ('scan_status', models.IntegerField(blank=True, null=True)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('total_dup', models.IntegerField(blank=True, null=True)),
                ('dockle_fatal', models.IntegerField(blank=True, null=True)),
                ('dockle_warn', models.IntegerField(blank=True, null=True)),
                ('inspec_info', models.IntegerField(blank=True, null=True)),
                ('inspec_pass', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dockle_scan_results_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_id', models.UUIDField(blank=True)),
                ('rescan_id', models.TextField(blank=True, null=True)),
                ('scan_date', models.TextField(blank=True)),
                ('project_id', models.UUIDField(blank=True)),
                ('vuln_id', models.UUIDField(blank=True)),
                ('false_positive', models.TextField(blank=True, null=True)),
                ('vul_col', models.TextField(blank=True)),
                ('dup_hash', models.TextField(blank=True, null=True)),
                ('vuln_duplicate', models.TextField(blank=True, null=True)),
                ('false_positive_hash', models.TextField(blank=True, null=True)),
                ('vuln_status', models.TextField(blank=True, null=True)),
                ('scanner', models.TextField(default='dockle', editable=False)),
                ('username', models.CharField(max_length=256, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('level', models.TextField(blank=True, null=True)),
                ('alerts', models.TextField(blank=True, null=True)),
            ],
        ),
    ]