import os
import pathlib
import requests

desktop_path = os.path.join(pathlib.Path.home(), "Desktop")
folder_name = "kromskii2"
folder_path = os.path.join(desktop_path, folder_name)

try:
    os.mkdir(folder_path)
    print(f"Папка с названием '{folder_name}' успешно создана на рабочем столе.")
except FileExistsError:
    print(f"Папка с названием '{folder_name}' уже существует на рабочем столе.")

file_url = "https://github.com/kromskii2/ccleaner/releases/download/1/maxresdefault.jpg"
file_name = file_url.split("/")[-1]
file_path = os.path.join(folder_path, file_name)

response = requests.get(file_url)
with open(file_path, "wb") as file:
    file.write(response.content)

print(f"Файл успешно скачан и сохранен в папке '{folder_name}' на рабочем столе.")
