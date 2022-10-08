''' This is the module. It actually does the work when we ask for things. For eg: if we says screenshot
this one actually takes and returns output'''
def screen_shot():
    from PIL import ImageGrab
    image = ImageGrab.grab()
    image.save("img.jpeg","JPEG")
    file = open("img.jpeg","rb")
    img_bytecode = file.read()
    return img_bytecode


def get_ip_local():
    import socket
    local_ip = socket.gethostbyname(socket.gethostname())
    return local_ip

def connection_status(what):
    import socket
    if what in 'hostname':
        hn=socket.gethostname()
        return hn
    elif what in 'status':
        while 1:
            import requests
            try:
                a = requests.get("https://google.com", timeout=8)
                return "Online"
            except :
                return "Offline"

def get_ip_public():
    import requests
    ip = requests.get('https://api.ipify.org', timeout=5).text
    return ip

def sysinfo(what):
    import platform

    if what in 'type':
        return platform.system()

    elif what in 'arch':
        # getting the 64 or 32 from outputted result
        osar = platform.architecture()
        osarch=osar[0]
        oa=osarch[0:2]
        if oa in '64':
            return 'x64'
        elif oa in '32':
            return 'x32'

    elif what in 'processor':
        pr = platform.processor()
        proc = pr[0:20]
        return proc

    elif what in 'ver':
        return platform.version()


def webcam():
    import os
    os.system('webcam.py')


def geo_location():
    import urllib, urllib.request
    url="http://ip-api.com/json/"

    try:
        locdata = urllib.request.urlopen(url, timeout=5).read()
        lc_decode = locdata.decode()
        return lc_decode

    except:
        k = "timedout"
        return k


def erase_data():
    return "Beta Feature"


def show_message(temp_message):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    # toaster.show_toast(owner_name,
    #                    message_to_show,
    #                    icon_path="custom.ico",
    #                    duration=10)
    toaster.show_toast("OWNER OF THIS LAPTOP",
                       temp_message)
