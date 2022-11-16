# Generated by Django 3.2.16 on 2022-11-16 15:59

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221114_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='BootcampModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('image', models.ImageField(default='', upload_to='bootcamp', verbose_name='bootcamp_image')),
                ('category', models.CharField(default='', max_length=100, verbose_name='category')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_link', models.CharField(default='', max_length=255, verbose_name='payment_link')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='team',
            name='instagram',
            field=models.CharField(default='instagram.com', max_length=200),
        ),
    ]
