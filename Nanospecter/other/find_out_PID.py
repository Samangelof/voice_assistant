import psutil

def info_run_app():
    for process in psutil.process_iter(['pid', 'name']):
        print(f"PID: {process.info['pid']}, Имя: {process.info['name']}")

info_run_app()

def get_pid_by_name(process_name):
    pid = None
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == process_name:
            pid = process.info['pid']
            break
    return pid


def search_PID(app_name):

    pid = get_pid_by_name(app_name)
    if pid is not None: print(f"PID процесса {app_name}: {pid}")
    else: print(f"Процесс {app_name} не найден")

# search_PID("chrome")

