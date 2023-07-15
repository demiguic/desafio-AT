# Generated by Django 4.2.3 on 2023-07-15 17:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nome',
        ),
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='inferior_limit',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='superior_limit',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='interval',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
