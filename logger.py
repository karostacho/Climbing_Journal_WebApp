import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log_error(self, error):
        self.log(f'Error: {error}')

    def log_message(self, message):
        self.log(f'Message: {message}')

    def log(self, log):
        file = open("log.txt", "a")
        self.logs.append(log)
        for log in self.logs:
            file.write(str(f'\n{datetime.datetime.now()} {log}'))
        file.close()