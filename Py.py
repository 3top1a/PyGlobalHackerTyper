# sudo pip install pynput
import threading
import pynput.keyboard
import time
import os.path

keyboard = pynput.keyboard.Controller()

# MAKE SURE IT ENDS WITH A '/'
pathToSamples = "./Samples/"

# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory#3207973
samples = [f for f in os.listdir(pathToSamples) if os.path.isfile(os.path.join(pathToSamples, f))]


# Run input() in a different thread
def bar():
    input()


thread = threading.Thread(target=bar)
thread.start()

for sample in samples:
    with open(pathToSamples + sample) as f:
        unParsedLines = f.readlines()

        # TODO parsing

        # Loop trough individual lines
        for line in unParsedLines:

            # Loop trough individual characters
            for char in line:
                try:
                    keyboard.press(str(char))
                    time.sleep(.02)
                    keyboard.release(str(char))
                    time.sleep(.02)
                except KeyboardInterrupt:
                    print('Interrupted')
                    os._exit(0)
                except:

                    # Releasing \n causes an exception so we are just ignore that
                    # FIXME
                    pass

            # End the line
            keyboard.press(pynput.keyboard.Key.enter)
            keyboard.release(pynput.keyboard.Key.enter)
