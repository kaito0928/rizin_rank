# Generated by Django 3.1.5 on 2021-02-03 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rizin_app', '0007_featherrank'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True, verbose_name='ニックネーム')),
                ('photo', models.ImageField(upload_to='', verbose_name='写真')),
                ('birthday', models.CharField(max_length=20, null=True, verbose_name='生年月日')),
                ('nationality', models.CharField(max_length=20, verbose_name='国籍')),
                ('height', models.IntegerField(verbose_name='身長')),
                ('mma_record', models.CharField(max_length=20, verbose_name='MMA戦績')),
                ('rizin_record', models.CharField(max_length=20, verbose_name='RIZIN戦績')),
            ],
            options={
                'verbose_name_plural': 'RightPlayer',
            },
        ),
        migrations.CreateModel(
            name='RightRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='作成者')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('eight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_eight', to='rizin_app.rightplayer')),
                ('five', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_five', to='rizin_app.rightplayer')),
                ('four', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_four', to='rizin_app.rightplayer')),
                ('nine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_nine', to='rizin_app.rightplayer')),
                ('one', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_one', to='rizin_app.rightplayer')),
                ('seven', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_seven', to='rizin_app.rightplayer')),
                ('six', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_six', to='rizin_app.rightplayer')),
                ('ten', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_ten', to='rizin_app.rightplayer')),
                ('three', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_three', to='rizin_app.rightplayer')),
                ('two', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='right_two', to='rizin_app.rightplayer')),
            ],
            options={
                'verbose_name_plural': 'RightRank',
            },
        ),
    ]
