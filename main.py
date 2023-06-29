import requests
import os
import socket
import time
import datetime
discordWebhookURL = ''
freemyiptoken = ''
freemyipURL = '' # ex YOUR_DOMAIN.freemyip.com
checkInterval = 60 # in seconds

def ipcheck():
    # check your current IP address 
    hazip = requests.get('https://icanhazip.com/')
    if hazip.status_code == 200:
        ipaddr = hazip.text
        # truncate the newline character
        ipaddr = ipaddr[:-1]
        print('Current IP: ' + ipaddr)
        # check your IP address from FreeMyIP
        # perform a DNS lookup on the URL to get the IP address
        freemyipaddr = socket.gethostbyname(freemyipURL)
        print('FreeMyIP IP: ' + freemyipaddr)
        # if the IP addresses are different, update FreeMyIP
        if ipaddr == freemyipaddr:
            print('IP addresses match')
        else:
            print('Updating FreeMyIP...')
            update = requests.get('https://freemyip.com/update?token=' + freemyiptoken + '&domain=' + freemyipURL)
            if update.status_code == 200:
                print('FreeMyIP updated!')
                discordUpdate(ipaddr, freemyipaddr, 'success')
            else:
                print('FreeMyIP update failed!')
                discordUpdate(ipaddr, freemyipaddr, 'failed')

def discordUpdate(newIP, oldIP, status):
    # timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    # send a discord notification
    if status == 'success':
        title = '**IP Address has been changed**'
        color = 16777215 # white
    elif status == 'failed':
        title = '**IP Address change failed**'
        color = 0xff0000 # red
    data = {
        "username" : "FreeMyIP Bot",
    }
    data["embeds"] = [
        {
            "title" : title,
            "description" : "**New IP: " + newIP + "**\n" + "**Old IP: " + oldIP + "**\n\n" + str(timestamp),
            "color" : color
        }
    ]
    print(requests.post(discordWebhookURL, json=data))

def main():
    while True:
        ipcheck()
        time.sleep(checkInterval)

if __name__ == '__main__':
    main()