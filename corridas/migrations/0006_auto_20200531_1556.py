# Generated by Django 3.0.6 on 2020-05-31 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corridas', '0005_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagem_categoria',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome_categoria',
            field=models.CharField(max_length=100),
        ),
    ]