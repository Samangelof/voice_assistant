import os
import psutil
import subprocess


class OpenApplication:
    def __init__(self, applications) -> None:
        self.applications = applications

    def open_application(self, app_name):
        try:
            if app_name in self.applications:
                subprocess.Popen(self.applications[app_name])
                print(f'{app_name} открыт')
        except Exception as Err:
            print(f'Ошибка при открытии приложения', {Err})


        
    def close_application(self, app_name):
        try:
            app_name_lower = app_name.lower()  # Преобразование к нижнему регистру
            result = subprocess.run(["taskkill", "/IM", app_name_lower, "/F"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{app_name} закрыт")
            else:
                print(f"Не удалось закрыть {app_name}:", result.stderr)
        except Exception as Err:
            print(f'Ошибка при закрытии {app_name}: {Err}')




    # def hide_application(self, app_name):
    #     try:
    #         process_name = app_name
            
    #         for process in psutil.process_iter(['pid', 'name']):
    #             if process.info['name'] == process_name:
    #                 pid = process.info['pid']
    #                 subprocess.run(["taskkill", "/PID", str(pid)])
    #                 print(f"{app_name} свернут")
    #                 break
    #         else:
    #             print(f"Процесс {app_name} не найден")
    #     except Exception as Err:
    #         print(f'Ошибка при сворачивании {app_name}: {Err}')