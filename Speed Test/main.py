from turtle import speed;
import speedtest;

speed = speedtest.Speedtest();

print("Speed Test\n");    

print("Download Speed")
downlaodSpeed = speed.download() / 8 / 1024 / 1024;
downlaodSpeed = str(downlaodSpeed);
print(downlaodSpeed[0:3] + " MB/S\n");

print("Upload Speed")
uploadSpeed = str(downlaodSpeed);
print(uploadSpeed[0:3] + " MB/S\n");

print("Ping");
print(speed.results.ping);
