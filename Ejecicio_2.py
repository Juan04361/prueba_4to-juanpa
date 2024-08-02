import serial

lectura = serial.Serial('COM8', 9600)

# Funciones 
def encender_led1():
    lectura.write(b'1')

def apagar_led2():
    lectura.write(b'2')


# Inicio de ciclo While
while True:
    comando = input("Escribe 'encender' para encender el LED o 'apagar' para apagarlo: ").strip().lower()
    
    if comando == 'encender1':
        encender_led1()
        print("servo1")
    elif comando == 'apagar1':
        apagar_led2()
        print("servo2")
  
    else:
        print("Comando no reconocido. Por favor escribe 'encender' o 'apagar'.")
