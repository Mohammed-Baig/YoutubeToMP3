from pytube import YouTube
import os
import urllib.request
import re

if __name__ == '__main__':
    song_list = []
    song = str(" ")

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'

    #get the list of songs you want to convert to MP3
    while (song != "yes"):
        song = input(str("Enter your song name here: ")).lower()
        song_list.append(song)
    song_list.remove("yes")

    #iterate through the list, convert each song to mp3 and download it in specified file
    for song in song_list:
        #in the event the song is more than one word, add + where spaces are to match the youtube query format
        song = song.replace(" ", "+")

        #get the youtube link of the song you searched up
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + song)
        vidID = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        vidID = "https://www.youtube.com/watch?v=" + vidID[0]

        #do the converstion and download the vid
        # url input from user
        yt = YouTube(vidID)
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")
