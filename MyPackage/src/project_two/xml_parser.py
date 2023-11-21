import requests
import pandas as pd
import xml.etree.ElementTree as ET
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

class XMLParser:
    def __init__(self, base_url):
        """
        Initialize the XMLParser with a base URL.

        Parameters:
            base_url (str): The base URL of the website to parse sitemaps from.
        """
        self.base_url = base_url

    def get_robots_txt(self):
        """
        Get the contents of the robots.txt file from the base URL.

        Returns:
            str: The contents of the robots.txt file.
        """
        try:
            response = requests.get(f"{self.base_url}/robots.txt")
            response.raise_for_status()
            return response.text
        except HTTPError as e:
            print(f"HTTP error while getting robots.txt: {e}")
            return ''
        except Exception as e:
            print(f"An error occurred while getting robots.txt: {e}")
            return ''

    def find_sitemaps(self, robots_txt):
        """
        Extract sitemap URLs from the robots.txt content.

        Parameters:
            robots_txt (str): The contents of the robots.txt file.

        Returns:
            list: A list of sitemap URLs.
        """
        sitemaps = []
        for line in robots_txt.splitlines():
            if line.startswith('Sitemap:'):
                sitemaps.append(line.split(': ')[1])
        return sitemaps

    def scrape_content(self, url):
        """
        Scrape the content from a given URL.

        Parameters:
            url (str): The URL to scrape content from.

        Returns:
            str: The scraped content as text.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            content_soup = BeautifulSoup(response.text, 'html.parser')
            if content_soup and hasattr(content_soup, 'text'):
                return content_soup.text
            else:
                return ''  # Return an empty string if no content found
        except HTTPError as e:
            print(f"HTTP error while scraping content: {e}")
            return ''
        except Exception as e:
            print(f"An error occurred while scraping content: {e}")
            return ''

    def parse_sitemap(self, sitemap_url):
        """
        Parse an XML sitemap and extract information.

        Parameters:
            sitemap_url (str): The URL of the XML sitemap to parse.

        Returns:
            pandas.DataFrame: A DataFrame containing URL, Last Modified, and Content columns.
        """
        try:
            response = requests.get(sitemap_url)
            response.raise_for_status()
            tree = ET.fromstring(response.content)
            scraped_data = []

            for url in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
                lastmod = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod').text
                content = self.scrape_content(loc)
                
                scraped_data.append({'URL': loc, 'Last Modified': lastmod, 'Content': content})
            
            return pd.DataFrame(scraped_data)
        except HTTPError as e:
            print(f"HTTP error while parsing sitemap: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of an error
        except Exception as e:
            print(f"An error occurred while parsing sitemap: {e}")
            return pd.DataFrame()  # Return an empty DataFrame for any other exception
# import requests
# import pandas as pd
# import xml.etree.ElementTree as ET
# from requests.exceptions import HTTPError
# from bs4 import BeautifulSoup

# class XMLParser:
    """
        Initialize the XMLParser with a base URL.

        Parameters:
            base_url (str): The base URL of the website to parse sitemaps from.
        """
    def __init__(self, base_url):
        self.base_url = base_url
        
        """
        Get the contents of the robots.txt file from the base URL.

        Returns:
            str: The contents of the robots.txt file.
        """
    def get_robots_txt(self):
        try:
            response = requests.get(f"{self.base_url}/robots.txt")
            response.raise_for_status()
            return response.text
        except HTTPError as e:
            print(f"HTTP error while getting robots.txt: {e}")
            return ''
        except Exception as e:
            print(f"An error occurred while getting robots.txt: {e}")
            return ''
        """
        Extract sitemap URLs from the robots.txt content.

        Parameters:
            robots_txt (str): The contents of the robots.txt file.

        Returns:
            list: A list of sitemap URLs.
        """
    def find_sitemaps(self, robots_txt):
        sitemaps = []
        for line in robots_txt.splitlines():
            if line.startswith('Sitemap:'):
                sitemaps.append(line.split(': ')[1])
        return sitemaps
    
        """
        Scrape the content from a given URL.

        Parameters:
            url (str): The URL to scrape content from.

        Returns:
            str: The scraped content as text.
        """

    def scrape_content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            content_soup = BeautifulSoup(response.text, 'html.parser')
            if content_soup and hasattr(content_soup, 'text'):
                return content_soup.text
            else:
                return ''  # Return an empty string if no content found
        except HTTPError as e:
            print(f"HTTP error while scraping content: {e}")
            return ''
        except Exception as e:
            print(f"An error occurred while scraping content: {e}")
            return ''

        """
        Parse an XML sitemap and extract information.

        Parameters:
            sitemap_url (str): The URL of the XML sitemap to parse.

        Returns:
            pandas.DataFrame: A DataFrame containing URL, Last Modified, and Content columns.
        """
    def parse_sitemap(self, sitemap_url):
        try:
            response = requests.get(sitemap_url)
            response.raise_for_status()
            tree = ET.fromstring(response.content)
            scraped_data = []

            for url in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
                lastmod = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod').text
                content = self.scrape_content(loc)
                
                scraped_data.append({'URL': loc, 'Last Modified': lastmod, 'Content': content})
            
            return pd.DataFrame(scraped_data)
        except HTTPError as e:
            print(f"HTTP error while parsing sitemap: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of an error
        except Exception as e:
            print(f"An error occurred while parsing sitemap: {e}")
            return pd.DataFrame()