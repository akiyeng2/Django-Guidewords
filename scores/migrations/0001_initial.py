# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('divID', models.CharField(max_length=100)),
                ('divNum', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_num', models.IntegerField()),
                ('player1Score', models.IntegerField(default=0)),
                ('player2Score', models.IntegerField(default=0)),
                ('isEntered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('wins', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('losses', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('spread', models.IntegerField(default=0)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scores.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField(default=1)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scores.Division')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='scores.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='scores.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Round'),
        ),
    ]
