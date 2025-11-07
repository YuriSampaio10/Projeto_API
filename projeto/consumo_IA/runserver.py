import os
import webbrowser
import time
from threading import Thread

def open_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:8000/usuarios/cadastro")

def run_server():
    os.system("python manage.py runserver")

if __name__ == "__main__":
    Thread(target=open_browser).start()
    run_server()
