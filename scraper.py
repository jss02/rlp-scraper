import requests
from bs4 import BeautifulSoup



def scrape_matches(url):
    rlp_url = "https://www.rugbyleagueproject.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    games = soup.find_all('a', class_='rlplnk')
    game_links = []
    for game in games:
        game_links.append(rlp_url + game['href'])
    
    return game_links

def scrape_game(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.text)

if __name__ == "__main__":
    matches = scrape_matches("https://www.rugbyleagueproject.org/seasons/nrl-2004/results.html")
    
    scrape_game(matches[0])