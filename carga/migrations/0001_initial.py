# Generated by Django 4.0.2 on 2022-02-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppTemp',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('idf', models.FloatField()),
                ('nom_tema', models.CharField(max_length=255)),
                ('num_area', models.IntegerField()),
                ('geom', models.IntegerField()),
            ],
            options={
                'db_table': 'App_Temp',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('car', models.CharField(max_length=255)),
                ('area', models.FloatField()),
                ('uf', models.CharField(max_length=255)),
                ('mun', models.CharField(max_length=255)),
                ('modulo_fiscal', models.FloatField()),
                ('tipo_imovel', models.CharField(max_length=255)),
                ('situacao', models.CharField(max_length=255)),
                ('condicao', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='TempAreaConsolidada',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('idf', models.IntegerField()),
                ('nom_tema', models.CharField(max_length=255)),
                ('geom', models.IntegerField()),
            ],
            options={
                'db_table': 'Temp_Area_Consolidada',
            },
        ),
        migrations.CreateModel(
            name='TempAreaImovel',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_imovel', models.CharField(max_length=255)),
                ('num_area', models.IntegerField()),
                ('cod_estado', models.CharField(max_length=255)),
                ('nom_munici', models.CharField(max_length=255)),
                ('num_modulo', models.IntegerField()),
                ('tipo_imovel', models.CharField(max_length=255)),
                ('situacao', models.CharField(max_length=255)),
                ('condicao_i', models.CharField(max_length=255)),
                ('geom', models.IntegerField()),
            ],
            options={
                'db_table': 'Temp_Area_Imovel',
            },
        ),
        migrations.CreateModel(
            name='TempReservaLegal',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('idf', models.IntegerField()),
                ('nom_tema', models.CharField(max_length=255)),
                ('num_area', models.IntegerField()),
                ('geom', models.IntegerField()),
            ],
            options={
                'db_table': 'Temp_Reserva_Legal',
            },
        ),
        migrations.CreateModel(
            name='TempVegetacaoNativa',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('idf', models.FloatField()),
                ('nom_tema', models.CharField(max_length=255)),
                ('num_area', models.IntegerField()),
                ('geom', models.IntegerField()),
            ],
            options={
                'db_table': 'Temp_Vegetacao_Nativa',
            },
        ),
    ]