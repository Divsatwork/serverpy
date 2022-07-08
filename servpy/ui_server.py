import os
from threading import Thread
from flask import Flask, send_from_directory
from .models import Server

class _UIServer(Server):
    def __init__(self, *args, **kwargs):
        pass

    def run(self):
        self.__run()

    def __run(self):
        app = Flask(__name__, static_folder='ui')

        # Serve React App
        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>')
        def serve(path):
            if path and os.path.exists(app.static_folder + '/' + path):
                return send_from_directory(app.static_folder, path)
            else:
                return send_from_directory(app.static_folder, 'index.html')

        print(f"Starting UI Service at localhost:8009")
        deamon = Thread(name='ui_server', target=app.run, kwargs={"use_reloader":False, "port":8009})
        deamon.start()
        print(f"UI Service daemon started. PID = {deamon.native_id}")
