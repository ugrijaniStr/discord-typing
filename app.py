import requests
import time

def startTyping(token, id):
    while True:
        url = f'https://discord.com/api/v9/channels/{id}/typing'
        xsp = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDEyIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDQiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImhyIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTgyOTgzLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDkyMSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="
        header = {
                "accept": "*/*",
                "accept-language": "en-US",
                "authorization": f'{token}',
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-GB",
                "x-super-properties": xsp,
                "referrer": f'https://discord.com/channels/1087443862106157147/{id}',
                "referrerPolicy": "strict-origin-when-cross-origin",
                "method": "POST",
                "mode": "cors",
                "credentials": "include"
        }

        send = requests.post(url, headers = header)
        if(send.status_code == 204):
            print(f'[{send.status_code}] Success!')
        time.sleep(3000)

startTyping('tuken','id')
