# Requires "requests" to be installed
import requests
import time
import sys
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.15)
typingPrint('∆ Requires Internet Connection!')
api_key = input('\n\nEnter Your API KEY\nGet it on remove.bg : ')
image_path = input('\n\nEnter Path Of Image: ')
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(image_path, 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': api_key},
)
if response.status_code == requests.codes.ok:
    typingPrint('\nProcessing...')
    time.sleep(3)
    name_save = input('\n\nImage name to be saved as\n[Do not include extentions of image]: ')
    with open(f'{name_save}.jpg', 'wb') as out:
        out.write(response.content)
        print('\nSuccess!')
else:
    print("Error:", response.status_code, response.text)