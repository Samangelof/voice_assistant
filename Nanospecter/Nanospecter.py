import time
import random
import pygetwindow as gw
import speech_recognition as sr

from nano_open_app import OpenApplication
from voice.voice_command import play_command
from application_path import (
    TG_PATH,
    OPERA_GX_PATH,
    GOOGLE_PATH,
    HELLO_ONE,
    HELLO_TWO,
    BYE_ONE,
    BYE_ONE
)

HELLO_AUDIO = [HELLO_ONE, HELLO_TWO]
hello_choice = random.choice(HELLO_AUDIO)

BYE_AUDIO = [BYE_ONE, BYE_ONE]
bye_choice = random.choice(BYE_AUDIO)


class NanospecterAssistant:
    

    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.applications = {
            'chrome': GOOGLE_PATH,
            'опера gx': OPERA_GX_PATH,
            'telegram': TG_PATH
        }
        self.open_app = OpenApplication(self.applications)

    def recognize_speech(self):
        with sr.Microphone() as source:
            print('Слушаю команду...')
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio, language="ru-RU")
                print("Вы сказали: " + text)
                return text.lower()
            except sr.UnknownValueError:
                print("Извините, не могу распознать вашу речь")
            except sr.RequestError as e:
                print("Ошибка при запросе к сервису распознавания речи; {0}".format(e))

    def run(self):
        while True:
            command = self.recognize_speech()
            # command = input('Что мне сделать ? \n>>> ').lower()

            # command move in .env
            # answers too in .env
            if command is not None: 
                if "привет" in command:
                    print('Привет. Слушаю команду...')
                    play_command(hello_choice, 5)

                elif 'открой' in command:
                    app_name = command.replace("открой", "").strip()
                    self.open_app.open_application(app_name)
                    print(command)

                elif 'закрой' in command:
                    app_name = command.replace("закрой", "").strip()
                    self.open_app.close_application(app_name)

                elif "сверни" in command:
                    self.open_app.hide_application(app_name)

                elif "покажи" in command:
                    all_windows = gw.getAllTitles()
                    print(f'{all_windows}, \n')

                elif 'стоп' in command or 'выход' in command:
                    print('Завершение процесса')
                    play_command('voice/close_process.mp3', 5)
                    break           
            else:
                print('Скажи, что мне сделать..')
                # play_command(bye_choice, 5) # giveme_task.mp3
                


nanospecter = NanospecterAssistant()
nanospecter.run()
