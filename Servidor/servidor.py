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
    playsound("audios/getPasword.wav")
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
        playsound("audios/wrongPassword.wav")
        print("Contrasena incorrecta")
        number1 = ""
        number2 = ""
        number3 = ""
        number4 = ""
        getPasssword (password)     

def readMessages():
    playsound("audios/readMessages.wav")
    print("No hay mensajes nuevos")
    
def printNumber(number):
    if number == '1':
        print('1')
        playsound("audios/uno.wav")
    elif number == '2':
        print('2')
        playsound("audios/dos.wav")
    elif number == '3':
        print('3')
        playsound("audios/tres.wav")
    elif number == '4':
        print('4')
        playsound("audios/cuatro.wav")
    elif number == '5':
        print('5')
        playsound("audios/cinco.wav")
    elif number == '6':
        print('6')
        playsound("audios/seis.wav")
    elif number == '7':
        print('7')
        playsound("audios/siete.wav")
    elif number == '8':
        print('8')
        playsound("audios/ocho.wav")
    elif number == '9':
        playsound("audios/nueve.wav")
        print('9')
    elif number == '0':
        playsound("audios/cero.wav")
        print('0')
    elif number == 'A':
        playsound("audios/A.wav")
        print('A')
    elif number == 'B':
        playsound("audios/B.wav")
        print('B')
    elif number == 'C':
        playsound("audios/C.wav")
        print('C')
    elif number == '#':
        playsound("audios/hastag.wav")
        print('#')
    else:
        playsound("audios/punto.wav")
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
    playsound("audios/newPassword.wav")
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