from pytube import YouTube
from colorama import init
from colorama.ansi import Fore
import os
import json
init(autoreset=True)

#Video download
def download(url):
    with open(".\data\config.json", "r") as file:
            config = json.load(file)
    folder = config['folder']
    video_obj = YouTube(url)
    stream = video_obj.streams.get_highest_resolution()
    stream.download(folder)

    print(Fore.GREEN + "The video was successfully downloaded to the folder: " + folder)
    os.system("pause")

#Creating a config.json file
def configSetup(folder):
    data = """
    {
        "folder" : ""
    }"""
    with open(".\data\config.json", "w+") as config:
        config.write(data)
    configWrite(folder)

#Creating a data folder
def FolderData():
    os.makedirs('.\data')
    Initialsetup()

#Writes the path to the download folder to the config
def configWrite(folder):
    with open('.\data\config.json') as f:
        cfg = json.load(f)
    cfg['folder'] = f"{folder}"
    with open('.\data\config.json', "w") as f:
        json.dump(cfg, f)
    main()
    
#Executed when the program is first launched
def Initialsetup():
    print(Fore.CYAN + 'Specify the folder to download the video.')
    Dfolder = input()
    print(Fore.CYAN + "-----------------------------------------------")
    configSetup(Dfolder)
    
#Main function
def main():
    if os.path.exists('.\data') == False:
        FolderData()
    else:
        if os.path.exists('.\data\config.json') == False:
            Initialsetup()
        else:
            print(Fore.CYAN + "Provide a link to the video.")
            video_url = input()
            download(video_url)


if __name__ == '__main__':
    main()
