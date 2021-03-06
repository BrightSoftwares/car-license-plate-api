# Generated by Django 2.0.7 on 2018-07-15 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0003_auto_20180715_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='plate',
            name='name',
        ),
        migrations.RemoveField(
            model_name='plate',
            name='surname',
        ),
        migrations.AddField(
            model_name='plate',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plates.Owner'),
            preserve_default=False,
        ),
    ]
