# Generated by Django 4.0.2 on 2022-03-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0003_alter_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apptemp',
            name='gid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='condicao',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tempareaconsolidada',
            name='gid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tempareaimovel',
            name='gid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tempreservalegal',
            name='gid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tempvegetacaonativa',
            name='gid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]