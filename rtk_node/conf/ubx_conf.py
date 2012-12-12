#!/usr/bin/env python
from serial import *
import binascii


def to_binstr( hexstr ):
    return binascii.unhexlify( join( hexstr.split() ) )

def send_cmd( ser, command ):
    cmd_str = to_binstr( command )
    ser.write( cmd_str )

ser = Serial( '/dev/ttyO2', 9600, timeout=1 )

# Send port configuration command
# USART1
# 0+1+2 In
# 0 Out
# 115200
# Autobauding
cmd = "B5 62 06 00 14 00 01 00 00 00 D0 08 00 00 00 C2 01 00 07 00 01 00 01 00 00 00 BF 76"
send_cmd( ser, cmd )

# Reconnect at 115200
ser.close()

ser = Serial( '/dev/ttyO2', 115200, timeout=1 )

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


