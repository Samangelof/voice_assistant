import pygame
import time



# pygame.init()

# pygame.mixer.music.load("voice/hello_lisen_command.mp3")
# pygame.mixer.music.play()


# time.sleep(5)

def play_command(file_path, duration=5):
    pygame.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    time.sleep(duration)

    pygame.quit()

# audio_file_path = "voice/hello_lisen_command.mp3"
# play_duration = 10  # Установите желаемую длительность в секундах
# play_command(audio_file_path, play_duration)


# import os


# def play_audio_with_windows_media_player(audio_file_path):
#     os.system(f'start wmplayer "{audio_file_path}"')

# audio_file_path = "C:/Users/Samangelof/Nanospecter/voice/hello.mp3" 
# play_audio_with_windows_media_player(audio_file_path)


