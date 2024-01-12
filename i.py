import requests
from bs4 import BeautifulSoup

def scrape_and_save(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Extract server information
        server_info = response.headers['Server']

        # Save server information to a text file
        with open('server_info.txt', 'w') as file:
            file.write(f"Server Information for {url}:\n")
            file.write(server_info)

        print(f"Server information saved to 'server_info.txt'")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    user_url = input("Enter the URL to scrape server information: ")
    scrape_and_save(user_url)
