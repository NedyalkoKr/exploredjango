# Generated by Django 3.0.7 on 2020-06-05 11:00

from django.db import migrations, models
import django.db.models.deletion
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0004_auto_20200605_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobbies',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='skills',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, autocomplete_view='myapp.views.hobbies_autocomplete', force_lowercase=True, help_text='Enter a comma-separated tag string', initial='coding, eating, gaming', max_count=5, to='tagging.Tagulous_Person_skills'),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=tagulous.models.fields.SingleTagField(_set_tag_meta=True, autocomplete_view='myapp.views.hobbies_autocomplete', blank=True, force_lowercase=True, initial='Mr, Mrs, Ms', null=True, on_delete=django.db.models.deletion.CASCADE, to='tagging.Tagulous_Person_title'),
        ),
    ]