# Generated by Django 3.0.6 on 2020-07-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tags', models.TextField()),
                ('b_des', models.TextField()),
                ('b_link', models.TextField()),
                ('i_des', models.TextField()),
                ('i_link', models.TextField()),
                ('e_des', models.TextField()),
                ('e_link', models.TextField()),
            ],
        ),
    ]