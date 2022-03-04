from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.CharField(max_length=255, blank=False)
    area = models.FloatField()
    uf = models.CharField(max_length=255)
    mun = models.CharField(max_length=255)
    modulo_fiscal = models.FloatField()
    tipo_imovel = models.CharField(max_length=255)
    situacao = models.CharField(max_length=255)
    condicao = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'Car'

        def __srt__(self):
            return self.car


class AppTemp(models.Model):
    gid = models.AutoField(primary_key=True)
    idf = models.FloatField()
    nom_tema = models.CharField(max_length=255)
    num_area = models.IntegerField()
    geom = models.IntegerField()

    class Meta:
        db_table = 'App_Temp'


class TempAreaConsolidada(models.Model):
    gid = models.AutoField(primary_key=True)
    idf = models.IntegerField()
    nom_tema = models.CharField(max_length=255)
    geom = models.IntegerField()

    class Meta:
        db_table = 'Temp_Area_Consolidada'


class TempAreaImovel(models.Model):
    gid = models.AutoField(primary_key=True)
    cod_imovel = models.CharField(max_length=255)
    num_area = models.IntegerField()
    cod_estado = models.CharField(max_length=255)
    nom_munici = models.CharField(max_length=255)
    num_modulo = models.IntegerField()
    tipo_imovel = models.CharField(max_length=255)
    situacao = models.CharField(max_length=255)
    condicao_i = models.CharField(max_length=255)
    geom = models.IntegerField()

    class Meta:
        db_table = 'Temp_Area_Imovel'


class TempReservaLegal(models.Model):
    gid = models.AutoField(primary_key=True)
    idf = models.IntegerField()
    nom_tema = models.CharField(max_length=255)
    num_area = models.IntegerField()
    geom = models.IntegerField()

    class Meta:
        db_table = 'Temp_Reserva_Legal'


class TempVegetacaoNativa(models.Model):
    gid = models.AutoField(primary_key=True)
    idf = models.FloatField()
    nom_tema = models.CharField(max_length=255)
    num_area = models.IntegerField()
    geom = models.IntegerField()

    class Meta:
        db_table = 'Temp_Vegetacao_Nativa'