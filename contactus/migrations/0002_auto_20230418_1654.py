# Generated by Django 3.2 on 2023-04-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Contact us'},
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
