# Generated by Django 2.1.8 on 2019-04-09 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('main', '0003_sectionindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='sectionindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='sectionpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='FlatPage',
        ),
        migrations.DeleteModel(
            name='SectionIndexPage',
        ),
        migrations.DeleteModel(
            name='SectionPage',
        ),
    ]
