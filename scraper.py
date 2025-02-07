import requests
from bs4 import BeautifulSoup

def get_matches(url):
    rlp_url = "https://www.rugbyleagueproject.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    game_links = soup.find_all('a', class_='rlplnk')
    print(game_links)

if __name__ == "__main__":
    get_matches("https://www.rugbyleagueproject.org/seasons/nrl-2004/results.html")