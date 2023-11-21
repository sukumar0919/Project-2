# WebInsights-MultiSourceAnalysis

## Description
This project encompasses various data extraction and analysis techniques, including XML parsing, API utilization, web scraping, and data analysis. The project aims to demonstrate the application of these techniques in extracting and processing data from different sources for further analysis.

## Tasks

### Part 1: XML Parsing
This task involves finding a website with a sitemap in XML format. A Python class is written to consume the robots.txt file of the website, find the sitemap(s), and parse the contents into a DataFrame.
Extract web content from BBC website using XML sitemaps
Collect URLs, last modification timestamps, and web page content
Create a structured DataFrame to store the extracted data

### Part 2: Using an API
This task involves finding a free API that provides data of interest. A Python class is built to make requests to the API and return a DataFrame for analysis.
Consume the USASpending API to retrieve top-tier agency data
Analyze the fetched data to identify agencies with the highest and lowest spending
Visualize the distribution of agency spending using histograms and box plots

### Part 3: Web Scraping
This task involves finding a website that allows scraping. A Python class is built using BeautifulSoup to scrape a dataset from the website.
Scrape book reviews from a specified web page using BeautifulSoup
Extract reviewer information, review dates, review titles, and review text
Organize the scraped data into a pandas DataFrame for further analysis


### Part 4: Analyze dataset from Part 2
This task involves performing basic analysis on the data collected from Part 2 . The results of the analysis are explained in a written narrative within formatted Markdown cells.
Perform basic analysis on the API-fetched data (Task 2)
Identify trends and patterns in agency spending
Analyze the distribution of budget authority amounts

## Installation
1. Install Python 3.x
2. Install the required Python libraries:
    pandas
    requests
    beautifulsoup4
    matplotlib

## Usage
1. Clone the project repository
2. Install the required Python libraries (as mentioned above)
3. For Task 1, run the xml_parser.py script
4. For Task 2, run the api_call.py script
5. For Task 3, run the web_scrapper.py script
6. For Task 4, run the analyze_data.py script


## License
MIT License
