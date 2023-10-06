import os
import pyttsx3
import subprocess
import speech_recognition as sr
from application_path import TG_PATH 
from other.open_app import open_telegram
import pygetwindow as gw
import psutil


def open_telegram(path):
    try:
        subprocess.Popen(path)
        print("Telegram открыт")
    except Exception as Err:
        print(f"Ошибка при открытии Telegram: {Err}")

def close_telegram():
    try:
        result = subprocess.run(["taskkill", "/IM", "Telegram.exe", "/F"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Telegram закрыт")
        else:
            print("Не удалось закрыть Telegram:", result.stderr)
    except Exception as Err:
        print(f'Ошибка при закрытии Telegram: {Err}')



def hide_telegram():
    try:
        # Имя процесса Telegram
        telegram_process_name = "Telegram.exe"
        
        # Поиск процесса Telegram
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == telegram_process_name:
                pid = process.info['pid']
                # Свернуть Telegram, отправив соответствующую команду
                subprocess.run(["taskkill", "/PID", str(pid)])
                print("Telegram свернут")
                break
        else:
            print("Процесс Telegram не найден")
    except Exception as Err:
        print(f'Ошибка при сворачивании Telegram: {Err}')

# Основной цикл
while True:
    user_input = input('>>> ').lower()
    if "привет" in user_input:
        print("Привет! Чем я могу помочь?")

    elif "покажи" in user_input:
        all_windows = gw.getAllTitles()
        print(f'{all_windows}, \n')

    elif "открой телеграм" in user_input:
        open_telegram(TG_PATH)

    elif "закрой телеграм" in user_input:
        close_telegram()

    elif "сверни телеграм" in user_input:
        hide_telegram()

    elif "стоп" in user_input:
        break
    else:
        print("Извините, я не понял ваш запрос.")


