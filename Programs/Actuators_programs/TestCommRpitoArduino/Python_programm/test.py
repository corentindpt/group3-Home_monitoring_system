import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
print("CTRL + C pour arrêter")

while True:
    action = input("Souhaitez-vous simuler la présence d'une personne connue ou inconnue ? (Connue = 1, inconnue = 0)")
    print(action)
    if action == '1':
        ser.write(b'1')
    else:
        ser.write(b'0')