import pyttsx3


class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.selected_voice = None

    def set_desired_voice(self, desired_voice_name):
        for voice in self.voices:
            if voice.name == desired_voice_name:
                self.selected_voice = voice
                self.engine.setProperty('voice', self.selected_voice.id)
                break

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

assistant = VoiceAssistant()

# SETUP VOICE
desired_voice_name = "Microsoft Zira Desktop - English (United States)"
assistant.set_desired_voice(desired_voice_name)

assistant.speak("Hello, this is my new voice")



# GET LIST VOICES
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(f"Имя: {voice.name}")
#     print(f"ID: {voice.id}")
#     print(f"Язык: {voice.languages}")
#     print(f"Пол: {voice.gender}")
#     print(f"Возраст: {voice.age}")
#     print("\n")