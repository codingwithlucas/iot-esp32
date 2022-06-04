Este é o projeto servidor DHT11 com ESP32.

Eu transformei uma placa ESP32 num servidor socket usando a biblioteca socket do Micropython. Este servidor possui uma página web que exibe
os valores de temperatura e umidade do ar medidos pelo sensor DHT11. Cada vez que o usuário acessa a página é realizada uma nova medição.

O sensor DHT11 está ligado aos pinos 3.3V, GND e 14 do ESP32.

This is the project DHT11 server with ESP32.

I built a socket webserver from an ESP32 board and the socket library available on Micropython. This server stores one web page
that shows the values of temperature and air humidity measured from DHT11 sensor. Each time the user goes to the page,
ESP32 does a new measurement.

The DHT11 sensor is connected to the ESP32 pins 3.3V, GND, and 14.
