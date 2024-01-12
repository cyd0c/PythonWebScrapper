# Web Scraper - Server Info

This Python script utilizes requests and BeautifulSoup to extract server information from a given URL. It makes an HTTP request to the specified website, retrieves the server details from the response headers, and saves this information to a text file named 'server_info.txt'.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required libraries by running: `pip install requests beautifulsoup4`
3. Run the script by executing: `python server_scraper.py`
4. Enter the URL when prompted to scrape server information.

## Example

```bash
python server_scraper.py
Enter the URL to scrape server information: https://example.com
