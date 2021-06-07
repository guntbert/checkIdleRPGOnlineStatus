# check my online status for the IdleRPG on libera.chat
import requests
from bs4 import BeautifulSoup

def get_xml():
    url = 'https://idlerpg.lolhosting.net/xml.php?player=heisenbug'
    response = requests.get(url)
    return response

def run_check():
    soup = BeautifulSoup(get_xml())
    soup.prettify()
if __name__ == '__main__':
    run_check()



