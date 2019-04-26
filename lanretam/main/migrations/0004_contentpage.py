# Generated by Django 2.1.8 on 2019-04-23 17:04

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('main', '0003_auto_20190423_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('table_caption', wagtail.core.blocks.CharBlock(help_text='Table caption', icon='fa-thumb-tack', required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='main/blocks/table_block.html')), ('sr_text', wagtail.core.blocks.TextBlock(icon='fa-universal-access', label='SR text', required=False)), ('map_block', wagtail.core.blocks.StructBlock([('map_title', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, verbose_name='Page content')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]