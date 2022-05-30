rgb_state = ""

def web_page():
    rgb_state = ""
    if redLed.value() == 1:
        rgb_state += "<p>Red led ON</p>"
    else:
        rgb_state += "<p>Red led OFF</p>"
         
    if greenLed.value() == 1:
        rgb_state += "<p>Green led ON</p>"
    else:
        rgb_state += "<p>Green led OFF</p>"
        
    if blueLed.value() == 1:
        rgb_state += "<p>Blue led ON</p>"
    else:
        rgb_state += "<p>Blue led OFF</p>"
        
    page = """
        <!DOCTYPE html>
            <html lang="EN">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link rel="icon" href="data:,">
                    <style>
                        html {
                            font-family: Helvetica;
                            display: inline-block;
                            margin: 0 auto;
                            text-align: center;
                        }
                        
                        h1 {
                            color: #0f3376;
                            padding: 2vh;
                        }
                        
                        p {
                            font-size: 1.3rem;
                        }
                        
                        .button {
                            display: inline-block;
                            border: none;
                            border-radius: 4px;
                            color: white;
                            padding: 16px 40px;
                            text-decoration: none;
                            font-size: 20px;
                            margin: 2px;
                            cursor: pointer;
                        }
                        
                        .off {
                            background-color: #484848;
                        }
                        
                        #redLedOn {
                            background-color: #D30000;
                        }
                        
                        #greenLedOn {
                            background-color: #028a0f;
                        }
                        
                        #blueLedOn {
                            background-color: #1338be;
                        }
                    </style>
                    <title>ESP32 controling RGB led</title>
                </head>
                <body>
                    <h1>ESP Web Server</h1>
                    <p>RGB state:</p>
                    <strong>""" + rgb_state +""" </strong>
                    <p><a href="/?redLed=on"><button id="redLedOn" class="button">Red led ON</button></a></p>
                    <p><a href="/?redLed=off"><button class="button off">Red led OFF</button></a></p>
                    <p><a href="/?greenLed=on"><button id="greenLedOn" class="button">Green led ON</button></a></p>
                    <p><a href="/?greenLed=off"><button class="button off">Green led OFF</button></a></p>
                    <p><a href="/?blueLed=on"><button id="blueLedOn" class="button">Blue led ON</button></a></p>
                    <p><a href="/?blueLed=off"><button class="button off">Blue led OFF</button></a></p>
                </body>
            </html>"""
    
    return page

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("It got a connection from %s" %(str(addr)))
    request = conn.recv(1024)
    request = str(request)
    print("Content: %s" %(request))
    redLedOn = request.find("/?redLed=on")
    redLedOff = request.find("/?redLed=off")
    greenLedOn = request.find("/?greenLed=on")
    greenLedOff = request.find("/?greenLed=off")
    blueLedOn = request.find("/?blueLed=on")
    blueLedOff = request.find("/?blueLed=off")
    if redLedOn == 6:
        print("Red led ON");
        redLed.value(1)
    if redLedOff == 6:
        print("Red led OFF")
        redLed.value(0)
    if greenLedOn == 6:
        print("Green led ON")
        greenLed.value(1)
    if greenLedOff == 6:
        print("Green led OFF")
        greenLed.value(0)
    if blueLedOn == 6:
        print("Blue led ON")
        blueLed.value(1)
    if blueLedOff == 6:
        print("Blue led OFF")
        blueLed.value(0)
    response = web_page()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()