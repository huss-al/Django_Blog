# Generated by Django 4.2.13 on 2024-06-19 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='appoved',
            new_name='approved',
        ),
    ]
