# Generated by Django 4.1.3 on 2022-12-08 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_products_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='categoryId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.category'),
        ),
    ]