import requests
from bs4 import BeautifulSoup
import pandas as pd

class WebScraper:
    """
    A class to scrape book reviews from a specific web page.

    Attributes:
    url: str
        The URL of the web page to scrape.

    Methods:
    scrape():
        Scrapes review information and returns it as a DataFrame.
    """

    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize empty lists to store scraped data
        reviewers = []
        review_dates = []
        review_titles = []
        review_texts = []

        # Find all review elements
        reviews = soup.find_all('div', {'class': 'aReview'})

        # Loop through each review and extract information
        for review in reviews:
            # Safely get the reviewer
            reviewer_tag = review.find('a')
            reviewer = reviewer_tag.text if reviewer_tag else 'No Reviewer'

            # Safely get the review date
            review_date = review.contents[4].strip() if len(review.contents) > 4 else 'No Date'

            # Safely get the review title
            subject_tag = review.find('b', text='Subject:')
            subject = subject_tag.find_next_sibling(text=True).strip() if subject_tag else 'No Subject'

            # Safely get the review text
            review_text_tag = review.find('div', {'class': 'breaker-breaker'})
            review_text = review_text_tag.text.strip() if review_text_tag else 'No Review Text'

            reviewers.append(reviewer)
            review_dates.append(review_date)
            review_titles.append(subject)
            review_texts.append(review_text)

        # Create a DataFrame from the scraped data
        review_data = pd.DataFrame({
            'Reviewer': reviewers,
            'Review Date': review_dates,
            'Review Title': review_titles,
            'Review Text': review_texts
        })

        return review_data
