# Generated by Django 4.0.5 on 2022-07-27 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lcicNews', '0015_h_lang'),
        ('lcicHome', '0011_menu_rename_id_user_group_gid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name_plural': 'Nav_Menu'},
        ),
        migrations.AlterModelOptions(
            name='user_group',
            options={'verbose_name_plural': 'GroupUser'},
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('SMID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(max_length=150)),
                ('nameE', models.CharField(max_length=150)),
                ('MID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicHome.menu')),
            ],
            options={
                'verbose_name_plural': 'Nav_Submenu',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('UID', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('nameL', models.CharField(max_length=150)),
                ('nameE', models.CharField(max_length=150)),
                ('surnameL', models.CharField(max_length=150)),
                ('surnameE', models.CharField(max_length=150)),
                ('insertDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('GID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicHome.user_group')),
                ('MID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberInfo', to='lcicNews.memberinfo')),
            ],
        ),
        migrations.CreateModel(
            name='GroupSubMenu',
            fields=[
                ('GSMID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insertDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('GID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicHome.user_group')),
                ('SMID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicHome.submenu')),
            ],
            options={
                'verbose_name_plural': 'GroupSubMenu',
            },
        ),
    ]