# ==================== A Simple Server =====================

import socket
import os
import time

def connect():
  # Creating a socket object 

  s = socket.socket()
  s.bind(('192.168.1.104', 9999))

  # Maximum number of connections in a queue (Backlog)
  s.listen(5)

  for _ in range(4):
    print('[*] Listening for connections')
    time.sleep(1)

  # First parameter(The connect object) 
  client, addr = s.accept()

  print(f'[+] We got connection from {addr[0]}:{addr[1]}')

  # Infinite loop
  while True:
    command = input(f'{os.getcwd()}>>>')
    if 'quit' in command:
      client.send('I would like to terminate'.encode('utf-8'))
      client.close()
      break
    else:
      client.send(command.encode())

      # Printing 1KB of the received data
      print(client.recv(2048).decode('utf-8'))



def main():
  connect()

main()
