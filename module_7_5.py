import os
import time

directory = '.'

# Перебор всех подкаталогов и файлов в указанной директории
for root, dirs, files in os.walk(directory):
    for file in files:

        filepath = os.path.join(directory, file)  # Формируем полный путь к файлу

        filetime = os.path.getmtime(filepath)   # Время последнего изменения

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Преобразование в читабельный формат

        filesize = os.path.getsize(filepath)    # Размер файла

        parent_dir = os.path.dirname(filepath)  # Родительская директория файла

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
