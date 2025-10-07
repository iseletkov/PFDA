import numpy as np
import pandas as pd
from sqlalchemy import create_engine 

# # Данные, организованные по столбцам
# data = {
#     'Группа': ['ПИ-101', 'ПИ-101', 'КИ-202'],
#     'ФИО': ['Иванов Алексей Сергеевич', 'Петрова Мария Дмитриевна', 'Сидоров Владимир Андреевич'],
#     'Год поступления': [2022, 2022, 2021],
#     'Средний балл': [4.7, 5.0, 4.3]
# }

# Создание DataFrame из словаря
# df = pd.DataFrame(data)
# print(df)

# Создание двигателя для подключения к базе данных PostgreSQL
engine = create_engine('postgresql://pfda:pfda_password@192.168.1.102:50000/pfda')

# Сохранение DataFrame в «my_table»
# df.to_sql('test', con=engine, if_exists='replace', index=False)

#Вся табличка полностью
# df = pd.read_sql_table('test', con=engine)  

# Набор данных по резултатам SQL запроса
df = pd.read_sql_query('select * from test where "Год поступления"=2022',con=engine)
print(df)