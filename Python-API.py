from time import sleep as wait
import requests
import random
import socket
import json
import os
  
session_id = -1

def check_data(recv):
  global session_id
  req = recv.decode()
  try:
    data = json.loads(req)

    print(data)

  except:
      status = 0
      

  try:
      user = data["user"]
      password = data["password"]

      if user == "Admin" and password == "password123":
          status = 1
          print("login Successful!")

          session_id = random.randint(10000, 99999)
          
      else:
          print("invalid login")
          status = 2
        
  except:
      status = 0

  return status
  
  

def listen(HOST = "127.0.0.1", PORT = 65432):
  global session_id
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      conn, addr = s.accept()
      with conn:
          print(f"Connected by {addr}")
          while True:
              data = conn.recv(1024)

              check = check_data(data)

              if check == 0:
                  conn.sendall(b"JSON ERROR!")

              elif check == 1:
                  conn.sendall(b"Connecting to Session: " + str(session_id).encode() + b"...")
                  
              elif check == 2:
                  conn.sendall(b"Login Invalid")
                  
                              
              if not data:
                  break
              
          
          conn.close()
          s.close()
  listen()



listen()
