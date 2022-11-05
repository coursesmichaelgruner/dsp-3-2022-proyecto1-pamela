from detectorDTMF import get_tone
from playsound import playsound

password = '1234'

def wait():
    playsound("audios/wait.wav")
    print("Marque cualquier tecla para comenzar")
    number = get_tone()
    print(number)
    numbers = ['1','2','3','4','5','6','7','8','9','0','A','B','C','#','.']
    if number  not in numbers:
        wait()
    

def ini():
    print("Bienvenido")
    playsound("audios/ini.wav")

def getPasssword (password):
    playsound("audios/getPassword.wav")
    print("Digite la contrasena")
    playsound("audios/primero.wav")
    print("Ingrese primer digito de la contrasena")
    number1 = get_tone()
    playsound("audios/segundo.wav")
    print("Ingrese segundo digito de la contrasena")
    number2 = get_tone()
    playsound("audios/tercero.wav")
    print("Ingrese tercer digito de la contrasena")
    number3 = get_tone()
    playsound("audios/cuarto.wav")
    print("Ingrese cuarto digito de la contrasena")
    number4 = get_tone()
    listenPassword = number1 + number2 + number3 + number4
    print(listenPassword )
    if listenPassword  != password:
        print("Contrasena incorrecta")
        number1 = ""
        number2 = ""
        number3 = ""
        number4 = ""
        getPasssword (password)     

def readMessages():
    print("No hay mensajes nuevos")
    
def printNumber(number):
    if number == '1':
        print('1')
    elif number == '2':
        print('2')
    elif number == '3':
        print('3')
    elif number == '4':
        print('4')
    elif number == '5':
        print('5')
    elif number == '6':
        print('6')
    elif number == '7':
        print('7')
    elif number == '8':
        print('8')
    elif number == '9':
        print('9')
    elif number == '0':
        print('0')
    elif number == 'A':
        print('A')
    elif number == 'B':
        print('B')
    elif number == 'C':
        print('C')
    elif number == '#':
        print('#')
    else:
        print('.')

def changePassword():
    playsound("audios/changePassword.wav")
    print("Digite la nueva contrasena")
    playsound("audios/primero.wav")
    print("Ingrese primer digito de la nueva contrasena")
    number1 = get_tone()
    playsound("audios/segundo.wav")
    print("Ingrese segundo digito de la nueva contrasena")
    number2 = get_tone()
    playsound("audios/tercero.wav")
    print("Ingrese tercer digito de la nueva contrasena")
    number3 = get_tone()
    playsound("audios/cuarto.wav")
    print("Ingrese cuarto digito de la nueva contrasena")
    number4 = get_tone()
    password = number1 + number2 + number3 + number4
    print("La nueva contrasena es: ")
    printNumber(number1)
    printNumber(number2)
    printNumber(number3)
    printNumber(number4)

    return password

def options():
    playsound("audios/options.wav")
    print("Digite 1 para leer sus mensajes o 2 para cambiar la contrasena")
    number = get_tone()
    if number == '1':
        readMessages()
    elif number == '2':
        changePassword()
    else:
        print("Digito invalido")
        options()


def main():
    wait()
    ini()
    getPasssword(password)
    options()
    

main()