# Generated by Django 3.0.2 on 2020-02-09 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='income/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.IncomeCategory')),
            ],
            options={
                'db_table': 'income',
            },
        ),
    ]
