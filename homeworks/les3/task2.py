def dataPerson(name=None, surname=None, birthyear=None, citylive=None, email=None, phonenumber=None):
    """
    Данные о пользователе:
    :param name: Имя
    :param surname: Фамилия
    :param birthyear: Год рождения
    :param citylive: Город проживания
    :param email: Email
    :param phonenumber: Телефонный номер
    :return: Вывод всех переданных данных
    """
    if not name:
        name = 'Данные отсутствуют'
    if not surname:
        surname = 'Данные отсутствуют'
    if not birthyear:
        birthyear = 'Данные отсутствуют'
    if not citylive:
        citylive = 'Данные отсутствуют'
    if not email:
        email = 'Данные отсутствуют'
    if not phonenumber:
        phonenumber = 'Данные отсутствуют'
    return (f'Имя: {name}, Фамилия: {surname}, Год рождения: {birthyear}, '
            f'Город проживания: {citylive}, E-mail: {email}, Номер телефона: {phonenumber}')

print(dataPerson(name='Василий', surname='Васильев', birthyear='2005', citylive='Питер', phonenumber=84195728342))