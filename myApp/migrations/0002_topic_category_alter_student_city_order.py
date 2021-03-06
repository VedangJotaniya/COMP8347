# Generated by Django 4.0.4 on 2022-05-26 17:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.CharField(default='Category001', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(choices=[('WS', 'Windsor'), ('CG', 'Calgary'), ('MR', 'Montreal'), ('VC', 'Vancouver')], default='WS', max_length=2),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levels', models.PositiveIntegerField(default=1)),
                ('order_status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Confirmed')], default=1)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.student')),
            ],
        ),
    ]
