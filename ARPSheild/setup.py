import os, sys, time

RED, GREEN, BLUE, YELLOW, WHITE, END= '\033[1;31m', '\033[1;32m', '\033[1;34m', '\033[1;33m', '\033[1;37m', '\033[0m'
spaces = " " * 76

sys.stdout.write(GREEN + spaces + """
                  ▄▄▄   ▄▄▄   ▄▄▄   ▄▄▄  ▄▄▄▄▄ ▄ ▄▄▄▄ ▄▄▄    ▄▄▄
                 █ . █ █ . \ █ . █ █ ▄▄█ █ █ █ █ █ ▄▄ █ █   █ ▄ █
                 █   █ █   / █  ▄█ █▄▄ █ █   █ █ █ ▄▄ █ █▄  █ █ █
                 █▄█▄█ █▄\▄\ █▄█   █▄▄▄█ █▄█▄█ █ █▄▄▄ █▄▄▄█ █▄▄▄█
    """ + END + BLUE +
    '\n' + '{}Protects you against ARP Spoof Attacks!{}'.format(RED,BLUE).center(98) +
    '\n' + 'Made With <3 by: {0}Aslam Muhammed ({1}Ash-Shaun{2})'.format(YELLOW, RED, YELLOW).center(104) +
'\n' + 'Version: {}1.0{} \n'.format(YELLOW, END).center(98))

print("")
inp = input("{}[-]{} You are about to install ARPShield. Do you want to continue? (Y/N)".format(YELLOW,WHITE)).capitalize()
print(inp)
if inp == "Y":
    print("{}[-]{}Please wait while the dependencies are installed. It may take a minute or two".format(YELLOW,WHITE))
    print("{}[-]{}Please enter the password if prompted".format(YELLOW,WHITE))
    time.sleep(2)
    os.system("sudo apt-get install python3-pip")
    os.system("pip3 install netifaces")
    os.system("sudo pip3 install scapy")
elif inp == "N":
    print("{}[-]{}Installation Aborted.{}".format(YELLOW, RED, WHITE))
else:
    print("{}[-]{}Unknown Input".format(YELLOW, WHITE))
    exit(0)

