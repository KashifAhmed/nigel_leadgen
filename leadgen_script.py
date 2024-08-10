import os
import pandas as pd
from serpapi import GoogleSearch
from dotenv import load_dotenv
import logging
import traceback
from datetime import datetime

# Create a timestamped log filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f'estate_agents_{timestamp}.log'

# Configure logging
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# Function to log and print messages
def log_and_print(message, level='info'):
    print(message)
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'warning':
        logging.warning(message)


try:
    # Load environment variables from .env file
    log_and_print("Loading environment variables from .env file...")
    load_dotenv()

    # Get the SerpApi key from environment variable
    api_key = os.getenv("SERPAPI_KEY")
    if api_key is None:
        raise ValueError("No SERPAPI_KEY found in environment variables.")
    log_and_print("Successfully loaded the SERPAPI_KEY.")


    # Function to fetch results from SerpApi with pagination
    def fetch_results(api_key, start=0, num_results=100):
        params = {
            'engine': 'google_maps',
            'q': 'estate agent',
            'll': '@51.507351,-0.127758,15.0z',  # Coordinates for London
            'type': 'search',
            'api_key': api_key,
            'start': start,
            'num': num_results  # Number of results to return (max 20 per page)
        }

        log_and_print(f"Fetching results starting at {start}...")
        search = GoogleSearch(params)
        return search.get_dict()


    # Initialize variables
    business_data = []
    start = 0
    num_results = 20  # Max number of results per page (as limited by SerpApi)
    total_results_fetched = 0

    log_and_print("Starting data fetching process...")

    # Fetch results iteratively
    while True:
        results = fetch_results(api_key, start=start, num_results=num_results)
        local_results = results.get('local_results', [])

        if not local_results:
            log_and_print("No more results found.")
            break

        for result in local_results:
            name = result.get('title')
            address = result.get('address')
            phone = result.get('phone')
            website = result.get('website', None)
            email = result.get('email', None)

            # Collect the data
            business_data.append({
                "Business Name": name,
                "Address": address,
                "Contact Number": phone,
                "Website": website,
                "Email Address": email
            })

        # Update counters
        total_results_fetched += len(local_results)
        start += num_results

        # Stop if fewer results were returned than requested, meaning the end of available data
        if len(local_results) < num_results:
            log_and_print("Fewer results than requested returned; ending fetch loop.")
            break

    # Export the data to a CSV file
    df = pd.DataFrame(business_data)
    output_filename = f'estate_agents{timestamp}.csv'
    df.to_csv(output_filename, index=False)

    log_and_print(f"Data exported to {output_filename} with {total_results_fetched} entries.")

except Exception as e:
    error_message = f"An error occurred: {str(e)}"
    log_and_print(error_message, level='error')
    log_and_print(traceback.format_exc(), level='error')
