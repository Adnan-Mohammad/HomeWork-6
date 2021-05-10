import socket
import urllib.request
import json

with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())



    country = (data['country_name'])
    city = (data['city'])
    postal = (data['postal'])
    state = (data['state'])





hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


while True:
    try:
        print('1 .look up my ip address')
        print('2 .look up info about specified ip')
        print('3 lookup info for my ip address')
        print('q - quit')
        data = int(input("what would you like to do "))

        if data == 1:
            print('your ip address is or enter q to go back to main menu ' + ip_address)
        elif data ==2:
            ip = int(input('enter your ip address'))
            print("your ip {} is located in {}".format(ip,country))

        elif data ==3:
            print("your ip is {} located in {},{}".format(ip_address,state,postal))




    except ValueError:
        print("thats an invalid ip, try again")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
