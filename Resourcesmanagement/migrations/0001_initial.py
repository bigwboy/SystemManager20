# Generated by Django 2.0.1 on 2018-01-16 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDomainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=50, verbose_name='域名')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '应用域名表',
                'verbose_name_plural': '应用域名表',
                'ordering': ['domain'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=30, verbose_name='应用')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '应用表',
                'verbose_name_plural': '应用表',
                'ordering': ['app'],
            },
        ),
        migrations.CreateModel(
            name='CDNTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CDN', models.CharField(max_length=30, verbose_name='CDN名称')),
                ('CDN_Remarks', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'CDN表',
                'verbose_name_plural': 'CDN表',
                'ordering': ['CDN'],
            },
        ),
        migrations.CreateModel(
            name='ControlDomainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ControlDomain', models.CharField(max_length=30, verbose_name='调度控制域名')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('CDN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resourcesmanagement.CDNTable')),
            ],
            options={
                'verbose_name': '调度控制域名表',
                'verbose_name_plural': '调度控制域名表',
                'ordering': ['ControlDomain'],
            },
        ),
        migrations.CreateModel(
            name='ControlIpTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ControlIp', models.GenericIPAddressField(protocol='ipv4', verbose_name='调度ip')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('CDN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resourcesmanagement.CDNTable')),
            ],
            options={
                'verbose_name': '调度控制ip表',
                'verbose_name_plural': '调度控制ip表',
                'ordering': ['ControlIp'],
            },
        ),
        migrations.CreateModel(
            name='CoverTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(max_length=50, verbose_name='覆盖情况')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '覆盖情况',
                'verbose_name_plural': '覆盖情况',
            },
        ),
        migrations.CreateModel(
            name='RegionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=30, verbose_name='域')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('CDN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resourcesmanagement.CDNTable')),
            ],
            options={
                'verbose_name': 'CDN域表',
                'verbose_name_plural': 'CDN域表',
                'ordering': ['region'],
            },
        ),
        migrations.CreateModel(
            name='restype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restype', models.CharField(max_length=50, verbose_name='类型')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '域名类型表',
                'verbose_name_plural': '域名类型表',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cdntable',
            unique_together={('CDN',)},
        ),
        migrations.AlterUniqueTogether(
            name='applicationtable',
            unique_together={('app',)},
        ),
        migrations.AddField(
            model_name='applicationdomaintable',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resourcesmanagement.ApplicationTable', verbose_name='应用'),
        ),
        migrations.AddField(
            model_name='applicationdomaintable',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resourcesmanagement.RegionTable', verbose_name='域'),
        ),
        migrations.AddField(
            model_name='applicationdomaintable',
            name='res_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resourcesmanagement.restype', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='applicationdomaintable',
            name='resoucescover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Resourcesmanagement.CoverTable', verbose_name='覆盖情况'),
        ),
        migrations.AlterUniqueTogether(
            name='regiontable',
            unique_together={('region',)},
        ),
        migrations.AlterUniqueTogether(
            name='controliptable',
            unique_together={('ControlIp',)},
        ),
        migrations.AlterUniqueTogether(
            name='controldomaintable',
            unique_together={('ControlDomain',)},
        ),
        migrations.AlterUniqueTogether(
            name='applicationdomaintable',
            unique_together={('domain', 'region', 'app')},
        ),
    ]