Este é o projeto de uma pequena estação meteorológica.
Para montá-lo é necessário ter uma placa ESP32, um módulo sensor DHT11,
um led RGB (ou três leds nas cores vermelho, verde e azul), três resistores
de 330 Ohm, jumpers macho-macho e duas protoboards.
A ideia é simples. Usar o sensor DHT11 para medir a temperatura e umidade
do ar de um ambiente e, após a medição, os dados são enviados para o servidor Thingspeak.
A placa ESP32 fica responsável por acessar o sinal do sensor e enviar os dados,
via wi-fi, para a conta Thingspeak especificada no programa.
Sinta-se livre para modificar o projeto de acordo com as suas necessidades.

This is the project of a small weather station.
To build it, you need a ESP32 board, a module DHT11,
one RGB led (or three leds, one of each following colors: red, green, blue),
three 330 Ohm resistors, male-male jumpers and two protoboards.
The idea behind is simple. The DHT11 sensor is used to measure the temperature and
air humidity of a room and, after the measurement, data is sent to the Thingspeak server.
The ESP32 board is responsable for getting signals from the sensor and send them,
through wi-fi, to the Thingspeak account specified on the code.
Feel free to modify the project according to your needs.
