import subprocess
import os
import atmos
import beaupy
import sys
from pystyle import Colors



#COLORS | Can add more, including dynamic colors.
RESET = Colors.reset
RED = Colors.red
GREEN = Colors.green
BLUE = Colors.blue
YELLOW = Colors.yellow
PURPLE = Colors.purple
CYAN = Colors.cyan
ORANGE = Colors.orange
PINK = Colors.pink
L_RED = Colors.light_red
L_GREEN = Colors.light_green
L_BLUE = Colors.light_blue
COLORS = [RED, L_RED, GREEN, L_GREEN, BLUE, L_BLUE, YELLOW, PURPLE, CYAN, ORANGE, PINK]


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
    if sys.platform == 'win32':
        cmd_arg = ["cmd.exe", "/c", "yt-dlp", "-o", "%(title)s.%(ext)s", "-f", "bestvideo+bestaudio", url]
    else:
        cmd_arg = ["yt-dlp", "-o", "%(title)s.%(ext)s", "-f", "bestvideo+bestaudio", url]

    try:
        subprocess.check_call(cmd_arg)
    except Exception as e:
        quit(RED + f"Oops, not a valid video url...\nError: {e}")
    clear()
    return print(GREEN + "Youtube video download complete!")



def p_list(url):
    if sys.platform == 'win32':
        cmd_arg = ["cmd.exe", "/c", "yt-dlp", "-o", "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s", url]
    else:
        cmd_arg = ["yt-dlp", "-o", "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s", url]

    try:
        subprocess.check_call(cmd_arg)
    except Exception as e:
        quit(RED + f"Oops, not a valid playlist url...\nError: {e}")
    clear()
    return print(GREEN + "Youtube playlist download complete!")



def audio(mp4file, mp3file):
    name, ext = os.path.splitext(mp3file)
    if not ext:
        mp3file = f"{mp3file}.mp3"

    if sys.platform == 'win32':
        cmd_arg = ["cmd.exe", "/c", "ffmpeg", "-i", mp4file, "-q:a", "0", "-map", "a", mp3file]
    else:
        cmd_arg = ["ffmpeg", "-i", mp4file, "-q:a", "0", "-map", "a", mp3file]

    try:
        subprocess.check_call(cmd_arg)
    except Exception as e:
        input(RED + f"An error has occured...\nError: {e}\n\nPress 'enter' to try again..." + RESET)
        mp3file = f"{mp3file}.mp3"
        try:
            cmd_arg[-1] = mp3file
            subprocess.check_call(cmd_arg)
        except Exception as e2:
            quit(RED + f"Oops, couldn't extract audio...\nError: {e2}")
    clear()



def main():
    while True:
        clear()
        options = ['Download Video?', 'Download Playlist?', 'Extract Audio?', 'Quit?']
        print(f'{logo()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
        option = beaupy.select(options, cursor_style="#ffa533")

        if not option:
            clear()
            quit(RED + "Keyboard Interuption Detected!\nGoodbye <3")


        if options[0] in option:
            video = beaupy.prompt("Video URL")
            if not video:
                clear()
                continue
            clear()
            print("Downloading video...")
            vid(video)
            input(GREEN + "Press enter to continue...")
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
            input(GREEN + "Press enter to continue...")
            clear()
            continue



        if options[2] in option:
            vod1mp4 = beaupy.prompt("File to extract audio from.")
            if not vod1mp4:
                clear()
                continue
            vod1mp4 = vod1mp4.replace('\\ ', ' ').strip().replace("'", '')

            audiomp3 = beaupy.prompt("Name of the audio file to be made. - (example_file.mp3)")
            if not audiomp3:
                clear()
                continue
            clear()
            audio(vod1mp4, audiomp3)
            input(GREEN + "Audio extraction complete!\nPress enter to continue...")
            clear()
            continue



        if options[3] in option:
            color2 = atmos.choice(COLORS)
            clear()
            quit(color2 + "Goodbye!")



if __name__ == '__main__':
    main()
