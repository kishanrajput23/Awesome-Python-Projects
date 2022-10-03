# import modules
import sys,socket

if len(sys.argv) == 2:
    host = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

print("=" * 50)
print("Scanning Port: " + host)
print("Scanning started at:" + str(datetime.now()))
print("=" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        if s.connect_ex(target, port)== 0:
            print("Port {} is open".format(port))
        s.close()

except socket.gainerror:
    print("\nHostname isn't resolved, try recheck you hostname")
except socket.error:
    print("\nServer didn't respond :(")
    sys.exit()
