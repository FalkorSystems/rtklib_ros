#!/usr/bin/env python
from serial import *
import binascii
import time

## {{{ http://code.activestate.com/recipes/496969/ (r1)
#convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)

#convert hex repr to string
def toStr(s):
    return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''
## end of http://code.activestate.com/recipes/496969/ }}}

def to_binstr( hexstr ):
    return binascii.unhexlify( ''.join( hexstr.split() ) )

def read_and_print( ser ):
    size = ser.inWaiting()
    read = ser.read( size )
    print "ack: " + toHex( read )

def send_cmd( ser, command ):
    cmd_str = to_binstr( command )
    print "sending: " + toHex( cmd_str )
    ser.write( cmd_str )
    time.sleep(1)
    read_and_print( ser )


start_baud = 9600
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

# Save configuration to Flash
cmd = "B5 62 06 09 0D 00 00 00 00 00 FF FF 00 00 00 00 00 00 03 1D AB"
send_cmd( ser, cmd )


