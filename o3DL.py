from pytube import YouTube
import subprocess
import os
from moviepy.editor import *
import colorama
import random
from alive_progress import alive_bar


#COLORS
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
COLORS = BLU, CYA, GRE, RED, MAG, LIRED, LIMAG, LIBLU, LICYA, LIGRE
colorama.init(autoreset=True)




# ---- Functuons ---- #


def logo() -> None:
    clear()
    color1 = random.choice(COLORS)
    print(color1 + """
---------------------------------------------------------------------------

                   ██████╗ ██████╗ ██████╗ ██╗     
                  ██╔═══██╗╚════██╗██╔══██╗██║     
                  ██║   ██║ █████╔╝██║  ██║██║     
                  ██║   ██║ ╚═══██╗██║  ██║██║     
                  ╚██████╔╝██████╔╝██████╔╝███████╗
                  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                        
      Made by Ori#6338 | @therealOri_ | https://github.com/therealOri

---------------------------------------------------------------------------\n      
    """)




def clear():
    os.system("clear||cls")


def vid(url):
    path = os.getcwd()
    try:
        with alive_bar(0) as bar:
            YouTube(url).streams.get_highest_resolution().download(path)
            bar()
    except Exception as e:
        exit(RED + f"Oops, not a valid video url...\nError: {e}")
    clear()
    return print(GRE + "Youtube video download complete!")


def p_list(url):
    try:
        subprocess.call(["yt-dlp", "-o", "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s", f"{url}"])
    except Exception as e:
        exit(RED + f"Oops, not a valid playlist url...\nError: {e}")
    clear()
    return print(GRE + "Youtube playlist download complete!")

 
def audio(mp4file, mp3file):
    videoclip = VideoFileClip(mp4file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3file)
    audioclip.close()
    videoclip.close()
    clear()
    return print(GRE + "Audio extraction complete!")


def main():
    while True:
        try:
            logo()
            color2 = random.choice(COLORS)
            options = int(input(color2 + "\n\n1. Download Video?\n2. Download Playlist?\n3. Extract audio?\n4. Quit?\n\nEnter: "))
        except Exception as e:
            clear()
            print(RED + f"Oops and error occured..Not an integer.\nError: {e}\n\n")
            input(GRE + "Press enter to continue...")
            clear()
            continue


        if options == 1:
            clear()
            video = input(color2 + "Video URL: ")
            clear()
            print(color2 + "Downloading video.....")
            vid(video)
            input(GRE + "Press enter to continue...")
            clear()
            continue
        elif options == 2:
            clear()
            plist = input(color2 + "Playlist URL: ")
            clear()
            print(color2 + "Downloading playlist.....(This will take awhile...)")
            p_list(plist)
            input(GRE + "Press enter to continue...")
            clear()
            continue



        elif options == 3:
            clear()
            vod1mp4 = input(color2 + "File to extract audio from.: ").replace('\\ ', ' ').strip().replace("'", '')
            audiomp3 = input(color2 + "Name of new audio file to be made.: ")
            clear()
            audio(vod1mp4, audiomp3)
            input(GRE + "Press enter to continue...")
            clear()
            continue
        elif options == 4:
            clear()
            exit(color2 + "Goodbye!")


        elif options < 1 or options > 4:
            clear()
            print(RED + "Unknown option...")
            input(GRE + "Press enter to continue...")
            clear()
            continue



if __name__ == '__main__':
    logo()
    main()
