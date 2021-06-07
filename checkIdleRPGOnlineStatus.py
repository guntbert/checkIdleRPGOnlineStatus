# check my online status for the IdleRPG on libera.chat
import requests
from bs4 import BeautifulSoup

name = 'heisenbug'

def get_xml(name):
    url = f'https://idlerpg.lolhosting.net/xml.php?player={name}'
    response = requests.get(url)
    return response.text

def run_check(name):
    soup = BeautifulSoup(get_xml(name), 'xml')
    status = soup.find('online').get_text()
    if status == '1':
        print(f'All is well. {name} is online')
    else:
        print(f'ALERT! {name} is OFFLINE!')
if __name__ == '__main__':
    run_check(name)



