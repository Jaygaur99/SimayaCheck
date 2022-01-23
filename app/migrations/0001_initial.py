# Generated by Django 3.1.13 on 2022-01-16 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('selling_price', models.PositiveIntegerField()),
                ('discounted_price', models.PositiveIntegerField()),
                ('discription', models.TextField()),
                ('category', models.CharField(choices=[('Ring', 'Ring'), ('Earring', 'Earring'), ('Bracelet', 'Bracelet'), ('Necklace', 'Neclace')], max_length=10)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
