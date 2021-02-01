# Generated by Django 3.1.5 on 2021-01-29 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rizin_app', '0006_bantamrank'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatherRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='作成者')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('eight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_eight', to='rizin_app.featherplayer')),
                ('five', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_five', to='rizin_app.featherplayer')),
                ('four', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_four', to='rizin_app.featherplayer')),
                ('nine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_nine', to='rizin_app.featherplayer')),
                ('one', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_one', to='rizin_app.featherplayer')),
                ('seven', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_seven', to='rizin_app.featherplayer')),
                ('six', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_six', to='rizin_app.featherplayer')),
                ('ten', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_ten', to='rizin_app.featherplayer')),
                ('three', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_three', to='rizin_app.featherplayer')),
                ('two', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featherrank_two', to='rizin_app.featherplayer')),
            ],
            options={
                'verbose_name_plural': 'FeatherRank',
            },
        ),
    ]
