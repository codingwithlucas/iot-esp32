from machine import Pin, reset
from time import sleep
from dht import DHT11
from network import WLAN, STA_IF
from urequests import post

# O LED vermelho simboliza tempo quente ou seco (mais do que 30°C ou umidade menor que 70%)
# O LED azul simboliza um tempo ameno (oposto do LED vermelho)
# O LED verde indica que as informações foram gravadas com sucesso no servidor Thingspeak
# Inicialmente todos os LEDs estão desligados

# The red LED is used to indicate when the weather is hot or dry (greater than 30°C or humidity less than 70%)
# The blue LED is used to indicate a warm weather (the opposite of the red LED)
# The green LED is used to indicate data has been sent successfully to the Thingspeak server
# In the begining, all LEDs are turn off

azulPin = Pin(18, Pin.OUT)
verdePin = Pin(19, Pin.OUT)
vermelhoPin = Pin(23, Pin.OUT)

azulPin.value(0)
verdePin.value(0)
vermelhoPin.value(0)

sensor = DHT11(Pin(4))

update_time = 1

def sinal_iniciar():
    """Utiliza os LEDs para indicar ao usuário que o programa iniciou.
       It blinks the LEDs to indicate for the user the program has started."""
    
    azulPin.value(1)
    sleep(0.200)
    azulPin.value(0)
    verdePin.value(1)
    sleep(0.200)
    verdePin.value(0)
    vermelhoPin.value(1)
    sleep(0.200)
    vermelhoPin.value(0)
    sleep(0.200)


def conectar_wifi(rede, senha):
    """A função recebe o nome e a senha de uma rede wi-fi e conecta o ESP32 nessa rede.
       Se tudo ocorrer bem, o LED verde pisca cinco vezes. Caso contrário o LED vermelho
       pisca cinco vezes.
       
       This function gets the name and password of a wi-fi network and connects ESP32 to it.
       If everything is okay, the green LED blinks five time. Otherwise the red LED
       blinks five times."""
    
    conexao = WLAN(STA_IF)
    conexao.active(True)
    conexao.connect(rede, senha)
    
    print("\nConectando à rede wi-fi...")
    while (conexao.isconnected() != True):
        vermelhoPin.value(1)
        sleep(0.100)
        vermelhoPin.value(0)
        sleep(0.100)    
    
    print("ESP32 conectado à internet")
    azulPin.value(0)
    vermelhoPin.value(0)
    verdePin.value(0)
    for i in range(10):
        verdePin.value(1)
        sleep(0.200)
        verdePin.value(0)
        sleep(0.200)
            
    return conexao
        
sinal_iniciar()
conexao = conectar_wifi("NET_2GA2CE5E", "B3A2CE5E")

while (conexao.isconnected() == True):
    # O primeiro try/except lida com a leitura de dados do sensor DHT11
    # The first try/except code block is about the readings of the DHT11 sensor
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        print("\nTemperatura: {}°C".format(temp))
        print("Umidade: {}%".format(hum))
        
        if (temp > 30 or hum < 70):
            vermelhoPin.value(1)
            azulPin.value(0)
            verdePin.value(0)
            print("CUIDE-SE, tempo quente ou seco")
        else:
            azulPin.value(1)
            vermelhoPin.value(0)
            verdePin.value(0)
            
        sleep(update_time)
    except:
        # Caso a conexão com o sensor seja perdida, a luz verde ficará acessa até que o sinal retorne
        # If the board is not getting data from the sensor, the green light will be on until the signal is back
        azulPin.value(0)
        vermelhoPin.value(0)
        verdePin.value(1)
        print("\nNão foi possível realizar a medição de temperatura e umidade")
        print("Uma nova tentativa ocorrerá em {} segundos".format(update_time))
        sleep(update_time)
        
    try:
        chamada = post("https://api.thingspeak.com/update?api_key=MGB6XNU6TW0L3YJC&field1={}&field2={}".format(temp, hum))
        chamada.close()
            
        print("Dados enviados com sucesso ao servidor Thingspeak")
        azulPin.value(0)
        vermelhoPin.value(0)
        verdePin.value(0)
        sleep(0.200)
        verdePin.value(1)
        sleep(0.200)
        verdePin.value(0)
    except:
        print("Não foi possível enviar os dados para o servidor Thingspeak")
        print("O programa será reiniciado em {} segundos".format(update_time))
        sleep(update_time)
        reset()
    
        
if (conexao.isconnected() == False):
    print("\nSem conexão com a internet")
    print("O programa será reiniciado")
    reset()
