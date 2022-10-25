from curses import baudrate
from enum import auto
from pymavlink import mavutil

address="udpin:localhost:14551"
#address="/dev/ttyACM0"
#address="/dev/ttyYHS1:115200"
vehicle=mavutil.mavlink.connection(address, baud=57600, autoreconnect=True)
vehicle.wait_heartbeat()
print("Bağlantı başarılı")
