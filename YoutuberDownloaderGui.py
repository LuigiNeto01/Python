from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
import os

sg.theme('Dark')

def download_video(youtube_url, choice, output_path, filename):
    yt = YouTube(youtube_url)
    if choice == '1':
        video_stream = yt.streams.filter(only_audio=True).first()
    elif choice == '2':
        video_stream = yt.streams.get_highest_resolution()
    else:
        return

    video_stream.download(output_path=output_path, filename=filename)

layout = [
    [sg.Text("Choose the directory: "), sg.InputText(key="output_folder"), sg.FolderBrowse()],
    [sg.Text("Vídeo Url: "), sg.In(key='link'), sg.Button("OK")],
    [sg.Text("Vídeo title: "), sg.Text('', size=(30, 1), key='video_title')],
    [sg.Radio('Audio', "choice", key='audio_choice', default=True),
     sg.Radio('Video', "choice", key='video_choice')],
    [sg.Text("Nome do arquivo: "), sg.InputText(key='filename')],
    [sg.Button('DOWNLOAD')]
]

window = sg.Window('YoutubeDownloader', layout)

while True:
    eventos, values = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'OK':
        yt = YouTube(values['link'])
        window['video_title'].update(yt.title)
    if eventos == 'DOWNLOAD':
        choice = '1' if values['audio_choice'] else '2'
        filename = values['filename'] + '.mp4' if choice == '2' else values['filename'] + '.mp3'
        download_video(values['link'], choice, values['output_folder'], filename)


window.close()
