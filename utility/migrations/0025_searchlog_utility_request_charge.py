# Generated by Django 4.2 on 2025-03-06 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0024_w_customer_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchlog_utility',
            fields=[
                ('search_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('bnk_code', models.CharField(max_length=100)),
                ('sys_usr', models.CharField(max_length=100)),
                ('edl_cusid', models.CharField(max_length=100)),
                ('wt_cusid', models.CharField(max_length=100)),
                ('tel_cusid', models.CharField(max_length=100)),
                ('proID_edl', models.CharField(max_length=100)),
                ('proID_wt', models.CharField(max_length=100)),
                ('proID_tel', models.CharField(max_length=100)),
                ('credittype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='request_charge',
            fields=[
                ('rec_sys_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('usr_session_id', models.CharField(max_length=100)),
                ('bnk_code', models.CharField(max_length=100)),
                ('chg_code', models.CharField(max_length=100)),
                ('chg_amount', models.CharField(max_length=100)),
                ('chg_unit', models.CharField(max_length=100)),
                ('sys_usr', models.CharField(max_length=100)),
                ('credit_type', models.CharField(max_length=100)),
                ('edl_cusid', models.CharField(max_length=100)),
                ('wt_cusid', models.CharField(max_length=100)),
                ('tel_cusid', models.CharField(max_length=100)),
                ('proID_edl', models.CharField(max_length=100)),
                ('proID_wt', models.CharField(max_length=100)),
                ('proID_tel', models.CharField(max_length=100)),
                ('red_reference_code', models.CharField(max_length=100)),
                ('rec_insert_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('search_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.searchlog_utility')),
            ],
        ),
    ]
