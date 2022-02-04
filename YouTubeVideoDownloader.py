from pytube import YouTube
from colorama import init
from colorama.ansi import Fore
import os
import json
init(autoreset=True)

#Скачивание видео
def download(url):
    with open(".\data\config.json", "r") as file:
            config = json.load(file)
    folder = config['folder']
    video_obj = YouTube(url)
    stream = video_obj.streams.get_highest_resolution()
    stream.download(folder)

    print(Fore.GREEN + "Видео успешно скачано в папку: " + folder)
    os.system("pause")

#Создание файла config.json
def configSetup(folder):
    data = """
    {
        "folder" : ""
    }"""
    with open(".\data\config.json", "w+") as config:
        config.write(data)
    configWrite(folder)

#Создание папки data
def FolderData():
    os.makedirs('.\data')
    Initialsetup()

#Записывает в конфиг путь к папке загрузки
def configWrite(folder):
    with open('.\data\config.json') as f:
        cfg = json.load(f)
    cfg['folder'] = f"{folder}"
    with open('.\data\config.json', "w") as f:
        json.dump(cfg, f)
    main()
    
#Выполняется при первом запуске программы
def Initialsetup():
    print(Fore.CYAN + 'Укажите папку для загрузки видео.')
    Dfolder = input()
    print(Fore.CYAN + "-----------------------------------------------")
    configSetup(Dfolder)
    
#Стартовая команда
def main():
    if os.path.exists('.\data') == False:
        FolderData()
    else:
        if os.path.exists('.\data\config.json') == False:
            Initialsetup()
        else:
            print(Fore.CYAN + "Укажите ссылку на видео.")
            video_url = input()
            download(video_url)


if __name__ == '__main__':
    main()