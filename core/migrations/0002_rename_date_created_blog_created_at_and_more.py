# Generated by Django 5.2 on 2025-04-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='music_field',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Bass', 'Bass'), ('Classical', 'Classical'), ('Instruments', 'Instruments'), ('Pop', 'Pop'), ('Jazz', 'Jazz'), ('Rock', 'Rock'), ('Western', 'Western'), ('Hip-Hop', 'Hip-Hop'), ('Electronic', 'Electronic'), ('Folk', 'Folk'), ('Blues', 'Blues'), ('Reggae', 'Reggae'), ('Country', 'Country'), ('Metal', 'Metal'), ('World', 'World')], default='Pop', max_length=32),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
