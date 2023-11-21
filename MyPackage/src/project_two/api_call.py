# api_handler.py
import requests
import pandas as pd

class APIHandler:
    """
    A class for handling API requests and responses.

    Attributes
    ----------
    base_url : str
        The base URL of the API.

    Methods
    -------
    fetch_data(endpoint: str, params: dict = None):
        Makes a GET request to the specified API endpoint and returns the data as a DataFrame.
    """
    """
     analyze_data(self, dataframe):
        Analyzes the data in the provided DataFrame and prints some basic statistics.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()

            # Assuming the API response is in JSON format
            data = response.json()

            # Extract the "results" field from the response
            results = data.get("results", [])

            # Convert the "results" data to a DataFrame
            dataframe = pd.DataFrame(results)

            return dataframe
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    
    def analyze_data(self, dataframe):
        if dataframe is not None:
        # Display basic statistics of the DataFrame
            print("Basic Data Statistics:")
            print(dataframe.describe())
            print("\n")  # Add an empty line
            
            # Number of Unique Agency Names
            unique_agency_names = dataframe['agency_name'].nunique()
            print(f"Number of Unique Agency Names: {unique_agency_names}")
            print("\n")  # Add an empty line

            # Total Spending Across All Agencies
            total_spending = dataframe['budget_authority_amount'].sum()
            print(f"Total Spending Across All Agencies: ${total_spending:.2f} billion")
            print("\n")  # Add an empty line

            # Average Spending per Agency
            average_spending_per_agency = total_spending / unique_agency_names
            print(f"Average Spending per Agency: ${average_spending_per_agency:.2f} billion")
            print("\n")  # Add an empty line

            # Agencies with the Highest Spending
            highest_spending_agencies = dataframe.nlargest(5, 'budget_authority_amount')
            print("Agencies with the Highest Spending:")
            print(highest_spending_agencies[['agency_name', 'budget_authority_amount']])
            print("\n")  # Add an empty line

            # Agencies with the Lowest Spending
            lowest_spending_agencies = dataframe.nsmallest(5, 'budget_authority_amount')
            print("Agencies with the Lowest Spending:")
            print(lowest_spending_agencies[['agency_name', 'budget_authority_amount']])
            print("\n")  # Add an empty line

            # Distribution of Spending Across Agencies (Histogram)
            import matplotlib.pyplot as plt
            plt.figure(figsize=(10, 6))
            plt.hist(dataframe['budget_authority_amount'], bins=20, edgecolor='k', alpha=0.7)
            plt.xlabel('Budget Authority Amount')
            plt.ylabel('Number of Agencies')
            plt.title('Distribution of Budget Authority Amounts')
            plt.grid(True)
            plt.show()
            print("\n")  # Add an empty line

            # Outliers in Spending (Box Plot)
            plt.figure(figsize=(10, 6))
            plt.boxplot(dataframe['budget_authority_amount'], vert=False)
            plt.xlabel('Budget Authority Amount')
            plt.title('Outliers in Budget Authority Amounts')
            plt.grid(True)
            plt.show()

        else:
             print("No data to analyze.")

# Additional write-up and insights can be provided based on the specific dataset and context.


