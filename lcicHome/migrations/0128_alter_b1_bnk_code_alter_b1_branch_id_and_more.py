# Generated by Django 5.0.6 on 2024-07-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0127_alter_b1_monthly_bnk_code_alter_b1_monthly_branch_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b1',
            name='bnk_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='b1',
            name='branch_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='b1',
            name='com_enterprise_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='customer_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lcicID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='loan_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_account_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_applied_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_class',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_credit_line',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_currency_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_exp_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_ext_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_insert_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_int_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_no_days_slow',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_open_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_outstanding_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_purpose_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_sys_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_term',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='lon_update_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b1',
            name='segmentType',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='b1',
            unique_together={('bnk_code', 'branch_id', 'customer_id', 'loan_id')},
        ),
    ]
