# #client
#
# client

import os
import cv2,pickle,time

import socket

cap = cv2.VideoCapture(0)

# Client socket created
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = ""
port = 12345
# Connection to server
s.connect(("192.168.43.158", 12345))

while True:
    stat, photo = cap.read()
    if stat:
        photo_data=pickle.dumps(photo)
        time.sleep(0.05)
        s.sendall(photo_data)
    else:
        print("error capturing")

    data = s.recv(9045600)
    try:
        photo=pickle.loads(data)
    except:
        print("Pickle error")
    if type(photo) is type(None):
        pass
    else:
        try:
            print("Photo received at Client")
            cv2.imshow("Server-SCREEN", photo)
            if cv2.waitKey(10) == 13:
                break
        except:
            pass

cv2.destroyAllWindows()
cap.release()
os.system("cls")

