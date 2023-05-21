import requests
import os
import socket
discordWebhookURL = ''
freemyiptoken = ''
freemyipURL = '' # ex YOUR_DOMAIN.freemyip.com
checkInterval = 60 # in seconds

def ipcheck():
    # check your current IP address 
    hazip = requests.get('https://icanhazip.com/')
    if hazip.status_code == 200:
        ipaddr = hazip.text
        print('Current IP: ' + ipaddr)
        # check your IP address from FreeMyIP
        # perform a DNS lookup on the URL to get the IP address
        freemyipaddr = socket.gethostbyname(freemyipURL)
        print('FreeMyIP IP: ' + freemyipaddr)
        # if the IP addresses are different, update FreeMyIP
        if ipaddr != freemyipaddr:
            print('Updating FreeMyIP...')
            update = requests.get('https://freemyip.com/update?token=' + freemyiptoken + '&domain=' + freemyipURL)
            if update.status_code == 200:
                print('FreeMyIP updated!')
            else:
                print('FreeMyIP update failed!')


def main():
    ipcheck()

if __name__ == '__main__':
    main()