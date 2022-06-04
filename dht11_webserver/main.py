def read_sensor():
    try:
        temperature = humidity = 0.0
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: %3.1f°C" %temperature)
        print("Humidity: %3.1f%%" %humidity)
        return temperature, humidity
    except:
        print("ESP32 couldn't read the sensor.")
        return 0, 0


def web_page(temperature, humidity):
    html = """
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width", initial-scale=1">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" crossorigin="anonymous">
                    <style>
                        html {
                            font-family: Arial;
                            display: inline-block;
                            margin: 0 auto;
                            text-align: center;
                        }
                        
                        h2 {
                            font-size: 3rem;
                        }
                        
                        p {
                            font-size: 3rem;
                        }
                        
                        .units {
                            font-size: 1.2rem;
                        }
                        
                        .dht11-label {
                            font-size: 1.5rem;
                            vertical-align: middle;
                            padding-bottom: 15px;
                        }
                        
                        #thermometer {
                            color: #059e8a;
                        }
                        
                        #tint{
                            color: #00add6;
                        }
                    </style>
                    <title>DHT11 server</title>
                </head>
                <body>
                    <main>
                        <h1>ESP32 DHT11 webserver</h1>
                        <p>
                            <i class="fas fa-thermometer-half" id="thermometer"></i>
                            <span class="dht11-label">Temperature</span>
                            <span>"""+str(temperature)+"""</span>
                            <sup class="units">&deg;C</sup>
                        </p>
                        <p>
                            <i class="fas fa-tint" id="tint"></i>
                            <span class="dht11-label">Humidity</span>
                            <span>"""+str(humidity)+"""</span>
                            <sup class="units">%</sup>
                        </p>
                    </main>
                </body>
            </html>
           """
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("It got a connection from %s" %str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    t, h = read_sensor()
    response = web_page(t, h)
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()
