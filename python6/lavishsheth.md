import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(5)

Output:- 
![Screenshot (12)](https://user-images.githubusercontent.com/109017996/193600341-8031ead3-d2c5-4527-91e0-fcbd253a314d.png)
