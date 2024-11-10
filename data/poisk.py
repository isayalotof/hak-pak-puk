import pandas as pd

file_path = 'config_file/db.xlsx'


def find_detail_info(article):
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return "Файл не найден."

    result = df[df['ДетальАртикул'].str.contains(article, na=False)]
    if result.empty:
        return "Деталь с указанным артикулом не найдена."

    info = ""
    for _, row in result.iterrows():
        info += f"""
        Артикул: {row['ДетальАртикул']}
        Порядковый Номер: {row['ПорядковыйНомер']}
        Наименование: {row['ДетальНаименование']}
        Номер Заказа: {row['ЗаказНомер']}
        Станция и Блок: {row['СтанцияБлок']}
        """
    return info
