import datetime

class Logger:
    def __init__(self):
        self.errors = []

    def display_error_message(self,  message = "Something went wrong"):
        print(message)

    def log_error(self, error, message):
        self.log(error)
        print(message)

    def log_message(self, message):
        self.log(message)

    def log(self, log):
        file = open("log.txt", "a")
        self.errors.append(log)
        for log in self.errors:
            file.write(str(f'\n{datetime.datetime.now()} {log}'))
        file.close()