# check my online status for the IdleRPG on libera.chat
import requests
from bs4 import BeautifulSoup

def get_xml():
    url = 'https://idlerpg.lolhosting.net/xml.php?player=heisenbug'
    response = requests.get(url)
    return response.text

def run_check():
    name = 'heisenbug'
    soup = BeautifulSoup(get_xml(), 'xml')
    status = soup.find('online').get_text()
    if status == '1':
        print(f'All is well. {name} is online')
    else:
        print(f'ALERT! {name} is OFFLINE!')
if __name__ == '__main__':
    run_check()



