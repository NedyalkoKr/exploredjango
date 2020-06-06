# Generated by Django 3.0.7 on 2020-06-05 10:18

from django.db import migrations, models
import django.db.models.deletion
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tagulous_Person_title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Tagulous_Person_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('skills', tagulous.models.fields.TagField(_set_tag_meta=True, force_lowercase=True, help_text='Enter a comma-separated tag string', max_count=5, to='tagging.Tagulous_Person_skills')),
                ('title', tagulous.models.fields.SingleTagField(_set_tag_meta=True, blank=True, initial='Mr, Mrs, Ms', null=True, on_delete=django.db.models.deletion.CASCADE, to='tagging.Tagulous_Person_title')),
            ],
        ),
    ]
