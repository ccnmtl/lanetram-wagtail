# Generated by Django 2.1.8 on 2019-04-17 21:06

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='main/blocks/table_block.html')), ('table_caption', wagtail.core.blocks.CharBlock(icon='fa-thumb-tack')), ('sr_text', wagtail.core.blocks.TextBlock(icon='fa-universal-access', label='SR text', required=False))], blank=True, verbose_name='Page content'),
        ),
    ]
