from threading import Thread
from flask import Flask


class test:
    def run(self):
        app = Flask(__name__, static_folder='ui')

        # Serve React App
        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>')
        def serve(path):
            return "Hello"

        # app.run(use_reloader=True, port=5000, threaded=True)

        print(f"StartingUI Service at localhost:8000")
        deamon = Thread(name='ui_server', target=app.run, args=("0.0.0.0", 8008), kwargs={'use_reloader':False, 'debug':False})
        # deamon.setDaemon(True) # This will die when the main thread dies
        deamon.start()
        print(f"UI Service daemon started. PID = {deamon.native_id}")

x = test()
x.run()