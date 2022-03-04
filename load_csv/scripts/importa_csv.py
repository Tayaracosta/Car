import csv

from carga.models import Car


def csv_to_list(filename: str) -> list:
    #  Lê um csv e retorna um OrdereDict.

    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        csv_data = [line for line in reader]

    return csv_data


def save_data(data):
    # Salva os dados

    aux = []
    for item in data:
        car = str(item.get('car'))
        area = item.get('area')
        uf = str(item.get('uf'))
        mun = str(item.get('mun'))
        modulo_fiscal = item.get('modulo_fiscal')
        tipo_imovel = str(item.get('tipo_imovel'))
        situacao = str(item.get('situacao'))
        condicao = str(item.get('condicao'))

        obj = Car(
            car=car,
            area=area,
            uf=uf,
            mun=mun,
            modulo_fiscal=modulo_fiscal,
            tipo_imovel=tipo_imovel,
            situacao=situacao,
            condicao=condicao,
        )
        aux.append(obj)
    Car.objects.bulk_create(aux)


def run():
    data = csv_to_list('csv/1700251.csv')
    save_data(data)
