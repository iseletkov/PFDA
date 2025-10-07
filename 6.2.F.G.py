import pandas as pd
def best(df):
    return df[(df['maths'] >= 4) & (df['physics'] >= 4) & (df['computer science'] >= 4)]

def need_to_work_better(df):
    return df[(df['maths'] == 2) | (df['physics'] == 2) | (df['computer science'] == 2)]

columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = need_to_work_better(journal)
print(journal)
print(filtered)