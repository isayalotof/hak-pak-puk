import pandas as pd


file_path = 'config_file/db.xlsx'

df = pd.read_excel(file_path)


# Функция для поиска информации по артикулу (должна быть импортирована или определена ранее)
def find_detail_info(article):
    # Загрузка данных из Excel и поиск информации
    df = pd.read_excel('your_excel_file.xlsx')
    result = df[df['ДетальАртикул'].str.contains(article, na=False)]

    if result.empty:
        return "Деталь с указанным артикулом не найдена."

    # Формирование текстового сообщения
    info = ""
    for index, row in result.iterrows():
        info += f"""
        Артикул: {row['ДетальАртикул']}
        Порядковый Номер: {row['ПорядковыйНомер']}
        Наименование: {row['ДетальНаименование']}
        Номер Заказа: {row['ЗаказНомер']}
        Станция и Блок: {row['СтанцияБлок']}
        """
    return info


# # Пример использования функции
# article_to_find = "1391-30-0108"  # Укажите артикул для поиска
# message = find_detail_info(article_to_find)
# print(message)
