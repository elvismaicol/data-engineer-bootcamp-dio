from datetime import date, time, datetime, timedelta


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.weekday())
    print(data_atual.date())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    # Converter String em data
    data_string1 = '01/01/2019'
    data_convertida1 = datetime.strptime(data_string1, '%d/%m/%Y')
    print(data_convertida1)
    data_string2 = '10/06/2020 17:45:30'
    data_convertida2 = datetime.strptime(data_string2, '%d/%m/%Y %H:%M:%S')
    print(data_convertida2)

    # Operaçõles com datas
    nova_data = data_convertida2 - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))


def trabalhando_com_time():
    horario = time(hour=18, minute=00, second=49)
    print(horario)
    horario_str = horario.strftime('%H %M %S')
    print(type(horario_str))


if __name__ == '__main__':
    # trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
