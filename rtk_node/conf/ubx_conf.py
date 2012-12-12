#!/usr/bin/env python
from serial import *
import binascii
import time

def to_binstr( hexstr ):
    return ''.join( hexstr.split() ).decode( 'hex' )

def read_and_print( ser ):
    size = ser.inWaiting()
    read_bytes = ser.read( size )
    print "ack: " + read_bytes.encode( 'hex' )

def send_cmd( ser, command ):
    cmd_str = to_binstr( command )
    print "sending: " + cmd_str.encode( 'hex' )
    ser.write( cmd_str )
    time.sleep(1)
    read_and_print( ser )


start_baud = 115200
end_baud = 115200

ser = Serial( '/dev/ttyO2', start_baud, timeout=1 )

# Send port configuration command
# USART1
# 0+1+2 In
# 0 Out
# 115200
# Autobauding
cmd_115200 = "B5 62 06 00 14 00 01 00 00 00 D0 08 00 00 00 C2 01 00 07 00 01 00 01 00 00 00 BF 76"


# USART1
# 0+1+2 In
# 0 Out
# 57600
# Autobauding
cmd_57600 = "B5 62 06 00 14 00 01 00 00 00 D0 08 00 00 00 E1 00 00 07 00 01 00 01 00 00 00 DD C1"

if end_baud == 115200:
    send_cmd( ser, cmd_115200 )
else:
    send_cmd( ser, cmd_57600 )

# Reconnect at end_baud
ser.close()
ser = Serial( '/dev/ttyO2', end_baud, timeout=1 )

# Send port configuration command
cmd = "B5 62 06 00 14 00 01 00 00 00 D0 08 00 00 00 C2 01 00 07 00 01 00 01 00 00 00 BF 76"
send_cmd( ser, cmd )

# Configure all other ports to nothing
cmd = "B5 62 06 00 14 00 00 00 00 00 D0 08 00 00 00 C2 01 00 00 00 00 00 01 00 00 00 B6 24"
send_cmd( ser, cmd )

cmd = "B5 62 06 00 14 00 02 00 00 00 D0 08 00 00 00 C2 01 00 00 00 00 00 01 00 00 00 B8 4C"
send_cmd( ser, cmd )

cmd = "B5 62 06 00 14 00 03 00 00 00 D0 08 00 00 00 C2 01 00 00 00 00 00 01 00 00 00 1D 84"

# Turn on RXM-RAW and RXM-SFRB
# RXM-RAW
cmd = "B5 62 06 01 06 00 02 10 00 01 00 00 20 D4"
send_cmd( ser, cmd )

# RXM-SFRB
cmd = "B5 62 06 01 06 00 02 11 00 01 00 00 21 D9"
send_cmd( ser, cmd )

# Set rate to 10Hz
cmd = "B5 62 06 08 06 00 64 00 05 00 01 00 7E 22"
send_cmd( ser, cmd )

# Turn NMEA on, UBX off
cmd_57600 = "B5 62 06 00 14 00 01 00 00 00 D0 08 00 00 00 E1 00 00 07 00 02 00 01 00 00 00 DE C7"
cmd_115200 = "B5 62 06 00 14 00 01 00 00 00 D0 08 00 00 00 C2 01 00 07 00 02 00 01 00 00 00 C0 7C"
if end_baud == 115200:
    send_cmd( ser, cmd_115200 )
else:
    send_cmd( ser, cmd_57600 )

# Save configuration to Flash
cmd = "B5 62 06 09 0D 00 00 00 00 00 FF FF 00 00 00 00 00 00 03 1D AB"
send_cmd( ser, cmd )


