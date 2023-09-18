from pytube import YouTube
import subprocess
import os
import colorama
import atmos
import beaupy
from beaupy.spinners import *


#COLORS
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
COLORS = [BLU, CYA, GRE, RED, MAG]
colorama.init(autoreset=True)




# ---- Functuons ---- #


def logo() -> None:
    clear()
    color1 = atmos.choice(COLORS)
    return color1 + """
---------------------------------------------------------------------------

                   ██████╗ ██████╗ ██████╗ ██╗     
                  ██╔═══██╗╚════██╗██╔══██╗██║     
                  ██║   ██║ █████╔╝██║  ██║██║     
                  ██║   ██║ ╚═══██╗██║  ██║██║     
                  ╚██████╔╝██████╔╝██████╔╝███████╗
                  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                        
       Made by @therealOri_ | https://github.com/therealOri
"""




def clear():
    os.system("clear||cls")



def vid(url):
    path = os.getcwd()
    try:
        spinner = Spinner(ARC, "Downloading video...")
        spinner.start()
        YouTube(url).streams.get_highest_resolution().download(path)
    except Exception as e:
        spinner.stop()
        quit(RED + f"Oops, not a valid video url...\nError: {e}")
    spinner.stop()
    clear()
    return print(GRE + "Youtube video download complete!")



def p_list(url):
    try:
        subprocess.call(["yt-dlp", "-o", "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s", f"{url}"])
    except Exception as e:
        quit(RED + f"Oops, not a valid playlist url...\nError: {e}")
    clear()
    return print(GRE + "Youtube playlist download complete!")



def audio(mp4file, mp3file):
    try:
        subprocess.check_call(["ffmpeg", "-i", mp4file, "-q:a", "0", "-map", "a", mp3file])
    except Exception as e:
        quit(RED + f"Oops, couldn't extract audio...\nError: {e}")
    clear()
    return print(GRE + "Audio extraction complete!")



def main():
    while True:
        clear()
        options = ['Download Video?', 'Download Playlist?', 'Extract Audio?', 'Quit?']
        print(f'{logo()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
        option = beaupy.select(options, cursor_style="#ffa533")

        if not option:
            clear()
            quit("Keyboard Interuption Detected!\nGoodbye <3")


        if options[0] in option:
            video = beaupy.prompt("Video URL")
            if not video:
                clear()
                continue
            clear()
            vid(video)
            input(GRE + "Press enter to continue...")
            clear()
            continue

        if options[1] in option:
            plist = beaupy.prompt("Playlist URL")
            if not plist:
                clear()
                continue
            clear()
            print(RED + "Downloading playlist....This will take some time..")
            p_list(plist)
            input(GRE + "Press enter to continue...")
            clear()
            continue



        if options[2] in option:
            vod1mp4 = beaupy.prompt("File to extract audio from.")
            if not vod1mp4:
                clear()
                continue
            vod1mp4 = vod1mp4.replace('\\ ', ' ').strip().replace("'", '')

            audiomp3 = beaupy.prompt("Name of new audio file to be made. - (example_file)")
            if not audiomp3:
                clear()
                continue
            clear()
            audio(vod1mp4, audiomp3)
            input(GRE + "Press enter to continue...")
            clear()
            continue



        if options[3] in option:
            color2 = atmos.choice(COLORS)
            clear()
            quit(color2 + "Goodbye!")



if __name__ == '__main__':
    main()
