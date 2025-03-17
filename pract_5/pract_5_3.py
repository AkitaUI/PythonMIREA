import csv
import datetime
import re
from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

messages = load_csv(r"messages.csv")
checks = load_csv(r"checks.csv")
statuses = load_csv(r"statuses.csv")

#3.1
time_data = [parse_time(row[4]) for row in messages[1:]]

weekday_counts = pd.Series([t.weekday() for t in time_data]).value_counts().sort_index()

weekday_labels = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
weekday_counts.index = [weekday_labels[i] for i in weekday_counts.index]

plt.figure(figsize=(10, 5))
plt.bar(weekday_counts.index, weekday_counts.values)
plt.xlabel('День недели')
plt.ylabel('Количество активностей')
plt.title('Распределение активности студентов по дням недели')
plt.xticks(rotation=45)
plt.show()

#3.2
# Извлечение часов из временных меток
hour_counts = pd.Series([t.hour for t in time_data]).value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(hour_counts.index, hour_counts.values)
plt.xlabel('Час суток')
plt.ylabel('Количество активностей')
plt.title('Распределение активности студентов по времени суток')
plt.xticks(range(24))
plt.show()

#3.3

# Группировка сообщений по задачам
task_messages = pd.Series([row[3] for row in messages[1:]]).value_counts()

plt.figure(figsize=(10, 5))
plt.bar(task_messages.index, task_messages.values)
plt.xlabel('Задача')
plt.ylabel('Количество сообщений')
plt.title('Количество сообщений по каждой задаче')
plt.xticks(rotation=90)
plt.show()

#3.4

# Загрузка данных без заголовков
messages_df = pd.DataFrame(messages)

# Переименование столбцов через индексы
messages_df.columns = ['student_id', 'group_id', 'task_id', 'message_id', 'time']

# Преобразование столбца времени в datetime
messages_df['time'] = pd.to_datetime(messages_df['time'], format='%Y-%m-%d %H:%M:%S.%f')

# Группировка данных по задачам и датам
activity_by_task = (
    messages_df
    .groupby([messages_df.iloc[:, 2], pd.Grouper(key='time', freq='D')])  # Группировка по задачам и дням
    .size()  # Подсчет количества сообщений
    .unstack(fill_value=0)  # Преобразование в таблицу с датами в качестве столбцов
)

# Визуализация активности для каждой задачи
plt.figure(figsize=(12, 6))
for task, data in activity_by_task.iterrows():
    plt.bar(data.index, data.values, label=f'Задача {task}', alpha=0.7)

plt.xlabel('Дата')
plt.ylabel('Количество сообщений')
plt.title('Активность студентов по задачам за период')
plt.xticks(rotation=45)
plt.legend(title="Задачи", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#3.5

# Подсчет сообщений по группам
group_messages = pd.Series([row[2] for row in messages[1:]]).value_counts()

plt.figure(figsize=(10, 5))
plt.bar(group_messages.index[:10], group_messages.values[:10])
plt.xlabel('Группа')
plt.ylabel('Количество сообщений')
plt.title('Группы с наибольшим количеством сообщений')
plt.xticks(rotation=45)
plt.show()

#3.6

processed_data = []
for row in checks:
    # Берем первый элемент строки (весь текст) и удаляем внешние кавычки
    clean_row = row[0].strip('"')
    # Разделяем строку по запятым, игнорируя экранированные кавычки
    parts = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', clean_row)
    # Удаляем лишние кавычки вокруг значений времени
    parts = [part.strip('"') for part in parts]
    processed_data.append(parts)

# Преобразование в DataFrame
checks_df = pd.DataFrame(processed_data, columns=['id', 'message_id', 'time', 'status'])

# Преобразование столбца времени в datetime
checks_df['time'] = pd.to_datetime(checks_df['time'], format='%Y-%m-%d %H:%M:%S.%f')

# Фильтрация только успешных проверок
# Предположим, что успешные проверки имеют статус '2' (на основе предоставленных данных)
successful_checks = checks_df[checks_df['status'] == '2']

# Подсчет успешных проверок по группам
# Предположим, что группы находятся в первом столбце ('id')
successful_checks_by_group = successful_checks['id'].value_counts()

# Визуализация
plt.figure(figsize=(10, 5))
plt.bar(successful_checks_by_group.index[:10], successful_checks_by_group.values[:10])
plt.xlabel('Группа')
plt.ylabel('Количество успешных решений')
plt.title('Группы с наибольшим количеством успешных решений')
plt.xticks(rotation=45)
plt.show()

#3.7

# Преобразование столбца 'status' в числовой формат
checks_df['status'] = pd.to_numeric(checks_df['status'], errors='coerce')

# Объединение данных checks_df и messages_df по 'message_id'
merged_df = pd.merge(checks_df, messages_df, on='message_id')

# Группировка данных по задачам и статусам
task_status_counts = merged_df.groupby(['task_id', 'status']).size().unstack(fill_value=0)

# Визуализация
task_status_counts.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.xlabel('Задача')
plt.ylabel('Количество проверок')
plt.title('Количество проверок по задачам и статусам')
plt.xticks(rotation=45)
plt.legend(title="Статус")
plt.tight_layout()
plt.show()

#3.8

def parse_achievements(achievements_str):
    """
    Преобразует строку достижений в список целых чисел.
    Если достижений нет, возвращает пустой список.
    """
    if not achievements_str or achievements_str == '[]':
        return []
    achievements = achievements_str.strip('[]').split(',')
    return [int(a.strip()) for a in achievements]

def count_achievements_by_group(statuses):
    """
    Подсчитывает количество достижений для каждой группы.
    Возвращает словарь, где ключ — группа, значение — количество достижений.
    """
    group_achievements = {}
    for row in statuses[1:]:  # Пропускаем заголовок
        group = row[2]  # Индекс группы
        achievements_str = row[5]  # Индекс достижений
        achievements = parse_achievements(achievements_str)
        if group not in group_achievements:
            group_achievements[group] = 0
        group_achievements[group] += len(achievements)
    return group_achievements

def find_top_groups(group_achievements, top_n=10):
    """
    Находит топ-N групп с максимальным количеством достижений.
    Возвращает отсортированный список кортежей (группа, количество достижений).
    """
    sorted_groups = sorted(group_achievements.items(), key=lambda x: x[1], reverse=True)
    return sorted_groups[:top_n]

group_achievements = count_achievements_by_group(statuses)

top_groups = find_top_groups(group_achievements, top_n=10)

top_group_names = [group for group, count in top_groups]
top_group_counts = [count for group, count in top_groups]

# Строим график
plt.figure(figsize=(10, 5))
plt.bar(top_group_names, top_group_counts)
plt.xlabel('Группа')
plt.ylabel('Количество достижений')
plt.title('Группы с наибольшим количеством достижений')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

def parse_achievements(achievements_str):
    """
    Преобразует строку достижений в список целых чисел.
    Если достижений нет, возвращает пустой список.
    """
    if not achievements_str or achievements_str == '[]':
        return []
    return [int(a.strip()) for a in achievements_str.strip('[]').split(',')]

def aggregate_data(statuses, key_func, value_func):
    """
    Агрегирует данные по заданному ключу и значению.
    key_func: функция для получения ключа (например, группа или студент).
    value_func: функция для получения значения (например, количество достижений или уникальные достижения).
    """
    aggregated = defaultdict(value_func)
    for row in statuses[1:]:
        key = key_func(row)
        achievements = parse_achievements(row[5])
        aggregated[key].update(achievements) if isinstance(aggregated[key], set) else aggregated[key].extend(achievements)
    return aggregated

def plot_top_entities(aggregated_data, title, xlabel, ylabel, top_n=10):
    """
    Строит график топ-N сущностей (групп или студентов).
    """
    sorted_data = sorted(aggregated_data.items(), key=lambda x: len(x[1]) if isinstance(x[1], set) else sum(x[1]), reverse=True)[:top_n]
    names = [str(key) for key, _ in sorted_data]
    counts = [len(value) if isinstance(value, set) else sum(value) for _, value in sorted_data]

    plt.figure(figsize=(10, 5))
    plt.bar(names, counts)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Загружаем данные из файла statuses.csv
statuses = load_csv('statuses.csv')

# 3.9: Топ-10 студентов
student_key_func = lambda row: (row[0], row[1], row[2])  # task, variant, group
student_value_func = list  # Список достижений
student_data = aggregate_data(statuses, student_key_func, student_value_func)
plot_top_entities(student_data, "Топ-10 студентов по количеству достижений", "Студент", "Количество достижений")

# 3.10: Группы с наибольшим количеством уникальных достижений
group_key_func = lambda row: row[2]  # group
group_value_func = set  # Множество уникальных достижений
group_data = aggregate_data(statuses, group_key_func, group_value_func)
plot_top_entities(group_data, "Группы с наибольшим количеством уникальных достижений", "Группа", "Количество уникальных достижений")