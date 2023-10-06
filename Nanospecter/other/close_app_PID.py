import psutil

import pygetwindow as gw

# CLOSE APPLICATION USING PID
def close_application(process_name):
    if not process_name.endswith(".exe"):
        process_name += ".exe"
    
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            pid = process.info['pid']
            try:
                process = psutil.Process(pid)
                process.terminate()
                print(f"{process_name} закрыт")
            except Exception as err:
                print(f"Не удалось закрыть {process_name}: {err}")
            break
    else:
        print(f"Процесс {process_name} не найден")

# close_application("chrome")



# CLOSE APP WINDOWS WITH TITILE
def close_chrome():
    chrome_window = gw.getWindowsWithTitle('Google Chrome')
    if chrome_window:
        # Получить первое найденное окно Chrome
        main_chrome_window = chrome_window[0]
        main_chrome_window.close()
        print("Главное окно Chrome закрыто")
    else:
        print("Главное окно Chrome не найдено")


close_chrome()


